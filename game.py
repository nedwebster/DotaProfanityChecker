from pydantic import BaseModel
from typing import List

from chat import Chat
from player import Player


class Game(BaseModel):
    """Class representing a single dota game."""
    match_id: int
    players: List[Player]
    chat: List[Chat]
    chat_assigned = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_player_slots(self) -> list:

        return [x.player_slot for x in self.players]

    def _get_player_chat_events(self) -> list:
        """Returns all chat events that are typed by players."""

        return [x for x in self.chat if x.is_player_chat]

    def _assign_chats(self):

        if not self.chat_assigned:
            for chat in self._get_player_chat_events():
                for player in self.players:
                    if chat.player_slot == player.player_slot:
                        player.add_chat_event(chat.key)
            self.chat_assigned = True
        else:
            print("Chat already assigned to players")

    def return_player_chats(self):
        return [
            (player.hero_id, player.combine_chat()) for player in self.players
            ]
