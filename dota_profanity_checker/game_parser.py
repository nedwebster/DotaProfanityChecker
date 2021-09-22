from dota_profanity_checker.open_dota_api import OpenDotaAPI
from dota_profanity_checker.chat_parser import ChatParser


class GameParser:

    game_api = OpenDotaAPI()
    chat_parser = ChatParser()

    def __init__(self, match_id):

        self.game = self._load_game(match_id)

    @classmethod
    def _load_game(cls, match_id):
        return cls.game_api.load_match(match_id)
