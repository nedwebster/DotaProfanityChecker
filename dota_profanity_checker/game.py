from pydantic import BaseModel, validator
from typing import List

from dota_profanity_checker.chat import Chat
from dota_profanity_checker.player import Player
from dota_profanity_checker.profanity_checker import ProfanityChecker


class Game(BaseModel):
    """Class representing a single dota game.

    WARNING! The chat attribute of this class refers to a list
    of chat.Chat() objects. The naming is confusing, but has been
    kept consistent with the data recieved from the opendota API.

    """
    match_id: int
    players: List[Player]
    chat: List[Chat] = None
    _chat_assigned: bool = False
    _profanity_checker = ProfanityChecker()

    class Config:
        underscore_attrs_are_private = True
        validate_assignment = True

    @validator("chat")
    def chat_present(cls, chat):
        if chat is None:
            print("Chat is empty for this game :(")
        return chat or []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def chat_assigned(self):
        return self._chat_assigned

    @chat_assigned.setter
    def chat_assigned(self, value):
        self._chat_assigned = value

    def _get_player_chat_events(self) -> list:
        """Returns all player chat events in this game."""
        return [x for x in self.chat if x.is_player_chat()]

    def _get_chatwheel_chat_events(self) -> list:
        """Returns all chatwheel chat events in this game."""
        return [x for x in self.chat if x.is_chatwheel_chat()]

    def _assign_chats_to_players(self):
        """Assigns all chat events in this game to relevant players.

        This updates the player.chat attribute for each player. If chats
        have already been assigned for this match, the process won't run.
        This is to prevent duplicated chat items being assigned to players.

        """

        if not self._chat_assigned:
            for chat in self._get_player_chat_events():
                for player in self.players:
                    if chat.player_slot == player.player_slot:
                        player.add_chat_event(chat.key)
            self._chat_assigned = True
        else:
            print("Chat already assigned to players")

    def get_player_chats(self) -> list:
        if not self._chat_assigned:
            self._assign_chats_to_players()

        return [
            (player.hero_id, player.combine_chat()) for player in self.players
        ]
