import requests
from game import Game


class Loader:
    """Class to pull game info from Dota API, given a specific match ID."""

    def __init__(self, match_id: str or int):

        def correct_match_id_type(match_id):
            """Corrects match_id type to be string if int is provided."""

            if isinstance(match_id, int):
                match_id = str(match_id)

            return match_id

        self.match_id = correct_match_id_type(match_id)

    def _get_request(self, match_id):
        """Makes the get request to the opendota api."""
        try:
            return requests.get(
                f"https://api.opendota.com/api/matches/{self.match_id}"
            )
        except requests.exceptions.ConnectionError:
            raise Exception("Cannot connect to dota API")

    def _validate_response(self, response: requests.models.Response):
        """Validates that a successful match id was provided, and a game was
        successfully collected."""

        if response.status_code == 200:
            print("Game successfully loaded!")
        else:
            raise ValueError("match_id {self.match_id} not found!")

    @staticmethod
    def _extract_game_data(response: requests.models.Response) -> dict:
        """Extracts the game info from the api response."""

        return response.json()

    def load_match(self) -> Game:
        """Pulls the match from the open dota API, validates the response,
        then initialises a Game object from the info."""

        response = self._get_request(self.match_id)
        self._validate_response(response)
        output = Game(**self._extract_game_data(response))

        return output
