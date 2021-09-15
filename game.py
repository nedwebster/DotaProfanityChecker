from pydantic import BaseModel
from typing import List

from chat import Chat
from player import Player


class Game(BaseModel):
    """Class representing a single dota game."""
    match_id: int
    players: List[Player]
    chat: List[Chat] = None
    _chat_assigned = False

    @property
    def chat_assigned(self):
        return self._chat_assigned

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            self._assign_chats_to_players

        return [
            (player.hero_id, player.combine_chat()) for player in self.players
            ]
