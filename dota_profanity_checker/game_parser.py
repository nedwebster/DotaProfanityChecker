from dota_profanity_checker.open_dota_api import OpenDotaAPI
from dota_profanity_checker.chat_parser import ChatParser
from dota_profanity_checker.profanity_checker import ProfanityChecker


class GameParser:
    """The main user API for profanity checking a given dota
    match id.

    """

    game_api = OpenDotaAPI()
    chat_parser = ChatParser()
    profanity_checker = ProfanityChecker()

    def __init__(self, match_id):
        self.game = self._load_game(match_id)

    @classmethod
    def _load_game(cls, match_id):
        return cls.game_api.load_match(match_id)

    def _get_game_chat(self):
        """Return the game chat from the classes game object."""
        return self.game.get_player_chats()

    def _format_game_chat(self, game_chat: list) -> dict:
        """Format the game chat using the injected chat_parser."""
        formatted_game_chat = {}

        for player_chat in game_chat:
            formatted_game_chat[player_chat[0]] = self.chat_parser.format_text(
                player_chat[1]
            )

        return formatted_game_chat

    def _profanity_check_game_chat(self, formatted_game_chat: dict) -> dict:
        """Check the formated game chat for profanities."""

        player_profanity_count = {}

        for player_id, formatted_chat in formatted_game_chat.items():
            player_profanity_count[player_id] = (
                self.profanity_checker.
                check_profanities(formatted_chat)
            )

        return player_profanity_count

    def profanity_check(self) -> dict:
        """The main call to check the profanity of a dota match."""
        game_chat = self._get_game_chat()
        formatted_game_chat = self._format_game_chat(game_chat)
        player_profanity_count = self._profanity_check_game_chat(
            formatted_game_chat
        )

        return player_profanity_count
