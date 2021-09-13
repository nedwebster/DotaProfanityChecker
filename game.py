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

    def _get_player_slots(self) -> list:

        return [x.player_slot for x in self.players]

    def get_player_chat_events(self) -> list:
        """Returns all chat events that are typed by players."""

        return [x for x in self.chat if x.is_player_chat]


if __name__ == "__main__":

    game_info = Loader(match_id=6176682329).load_match()

    my_game = Game(**game_info)

    game_chat = my_game.get_player_chat_events()

    print(game_chat)
