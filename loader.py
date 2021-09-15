import requests
from game import Game


class Loader:
    """Class to pull game info from Dota API, given a specific match ID."""

    def __init__(self):

        self._dota_api_url = "https://api.opendota.com/api/matches/"

    def _get_request(self, match_id):
        """Makes the get request to the opendota api."""
        try:
            return requests.get(
                self._dota_api_url + match_id
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
            raise ValueError(f"match_id {match_id} not found!")

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
