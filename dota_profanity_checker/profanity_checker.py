from dota_profanity_checker.chat_parser import ChatParser


class ProfanityChecker:
    """Profanity checker class."""

    chat_parser = ChatParser()

    def __init__(self):

        def load_profanity_list() -> str:
            """Loads the curse words from the local text file."""

            with open("./lookups/curse_words.txt", "r") as f:
                return f.read()

        def format_profanity_list(profanity_list: str) -> list:
            """Formats the profanity list."""

            return profanity_list.split("\n")

        profanity_list = load_profanity_list()
        self._profanity_list = format_profanity_list(profanity_list)

    @property
    def profanity_list(self):
        return self._profanity_list

    def check_profanities(self, words: list) -> dict:
        """Checks a list of words against the loaded profanity list Return
        a dictionary of curse word counts."""

        profanities = {}
        for profanity in self._profanity_list:
            word_count = words.count(profanity)
            if word_count != 0:
                profanities[profanity] = word_count
        return profanities
