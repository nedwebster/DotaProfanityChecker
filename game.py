from pydantic import BaseModel
from typing import List

from chat import Chat
from player import Player
from loader import Loader


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


if __name__ == "__main__":

    game_info = Loader(match_id=6176682329).load_match()

    my_game = Game(**game_info)

    my_game._assign_chats()

    print(my_game.players)
