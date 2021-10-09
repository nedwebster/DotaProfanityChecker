import http
import requests

from dota_profanity_checker.game import Game


class OpenDotaAPI:
    """Class to pull game info from Dota API, given a specific match ID."""

    DOTA_API_URL = "https://api.opendota.com/api/matches/"

    @classmethod
    def _get_request(cls, match_id):
        """Makes the get request to the opendota api."""
        try:
            return requests.get(
                cls.DOTA_API_URL + match_id
            )
        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to dota API")

    @staticmethod
    def _validate_response(match_id: str, response: requests.models.Response):
        """Validates that a successful match id was provided, and a game was
        successfully collected."""

        if response.status_code == 200:
            print("Game successfully loaded!")
        else:
            code = response.status_code
            message = http.HTTPStatus(code).name
            raise ValueError(f"{message}: {code}")

    @staticmethod
    def _extract_game_data(response: requests.models.Response) -> dict:
        """Extracts the game info from the api response."""

        return response.json()

    @staticmethod
    def _correct_match_id_type(match_id):
        """Corrects match_id type to be string if int is provided."""

        if isinstance(match_id, int):
            match_id = str(match_id)

        return match_id

    def load_match(self, match_id: str) -> Game:
        """Pulls the match from the open dota API, validates the response,
        then initialises a Game object from the info."""

        match_id = self._correct_match_id_type(match_id)

        response = self._get_request(match_id)
        self._validate_response(match_id, response)
        output = Game(**self._extract_game_data(response))

        return output
