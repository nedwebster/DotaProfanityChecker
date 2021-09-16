from pydantic import BaseModel, validator
from typing import List

from chat import Chat
from player import Player
from profanity import ProfanityChecker


class Game(BaseModel):
    """Class representing a single dota game."""
    match_id: int
    players: List[Player]
    chat: List[Chat] = None
    _chat_assigned: bool = False
    _profanity_checker = ProfanityChecker()

    class Config:
        underscore_attrs_are_private = True
        validate_assignment = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @validator("chat")
    def set_chat(cls, chat):
        if chat is None:
            print("Chat is empty for this game :(")
        return chat or []

    @property
    def chat_assigned(self):
        return self._chat_assigned

    @chat_assigned.setter
    def chat_assigned(self, value):
        self._chat_assigned = value

    def _get_player_chat_events(self) -> list:
        """Returns all chat events that are typed by players."""

        return [x for x in self.chat if x.is_player_chat]

    def _assign_chats_to_players(self):
        """Assigns all chat events to the relevant player.

        This updates the player.chat attribute for each player. If chats
        have already been assigned for this match, the process won't run.

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

    @staticmethod
    def _is_profanity_clean(profanity_record: dict) -> bool:

        profanity_count = sum([
            len(sub_dict) for sub_dict in profanity_record.values()
        ])

        return profanity_count == 0

    def profanity_check(self):
        """Checks the players chat for any profanity."""

        profanity_record = {}
        for player_chat in self.get_player_chats():
            profanity_record[player_chat[0]] = (
                self._profanity_checker.analyse_text(player_chat[1])
            )

        if self._is_profanity_clean(profanity_record):
            print("No profanity found, what lovely players :)")
        else:
            print(f"Bad language detected!\n{profanity_record}")
