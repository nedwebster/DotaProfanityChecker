from collections import namedtuple
from pydantic import BaseModel

from loader import Loader


class Game(BaseModel):
    """Class representing a single dota game."""
    match_id: int
    players: list
    chat: list

    def _get_player_slots(self):

        return [x["player_slot"] for x in self.players]

    @staticmethod
    def _is_player_chat(chat_event: dict) -> bool:
        """Checks if chat_event is a player chat."""

        return chat_event["type"] == "chat"

    @classmethod
    def _drop_chat_events(cls, chat_events: list) -> list:
        """Drops non-player chat events"""

        return [x for x in chat_events if cls._is_player_chat(x)]

    @staticmethod
    def _format_chat_events(chat_events: list) -> list:
        """Format chat events into namedtuples."""

        ChatItem = namedtuple("player_chat", ["player_slot", "key"])

        return [ChatItem(x["player_slot"], x["key"]) for x in chat_events]

    def collate_chat_events(self):
        """Collects all player chat events, and format them for ease of
        use elsewhere."""

        chat_events = self._drop_chat_events(self.chat)

        return self._format_chat_events(chat_events)


if __name__ == "__main__":

    game_info = Loader(match_id=6176682329).load_match()

    my_game = Game(**game_info)

    game_chat = my_game.collate_chat_events()

    print(game_chat)
