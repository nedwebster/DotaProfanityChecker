import string


class ProfanityChecker:
    """Profanity checker class."""

    def __init__(self):

        def load_profanity_list() -> str:
            """Loads the curse words from the local text file."""

            with open("lookups/curse_words.txt", "r") as f:
                return f.read()

        def format_profanity_list(profanity_list: str) -> list:
            """Formats the profanity list."""

            return profanity_list.split("\n")

        profanity_list = load_profanity_list()
        self._profanity_list = format_profanity_list(profanity_list)
        self._punctuation = set(string.punctuation)

    def _remove_punctuation(self, text: str) -> str:
        """Removes punctuation from text."""

        return "".join(x for x in text if x not in self._punctuation)

    def _format_text(self, text: str) -> str:
        """Format text. Converts to lower case, then removes punctuation."""

        text = text.lower()
        text = self._remove_punctuation(text)
        return text

    def _get_words(self, text: str) -> list:
        """Splits a formatted text string into seperate words."""
        for ch in text:
            if ch in self._punctuation:
                raise ValueError(
                    "text contains punctuation, clean before generating words"
                )
        return text.split(" ")

    def _check_profanities(self, words: list) -> dict:
        """Checks a list of words against the loaded profanity list."""
        profanities = {}
        for profanity in self._profanity_list:
            word_count = words.count(profanity)
            if word_count != 0:
                profanities[profanity] = word_count
        return profanities

    def analyse_text(self, text: str) -> dict:
        """Checks a given text string for profanities. First it formats the
        string, splits the string into words, and then counts profanities
        from a pre-defined list of curse words."""

        text = self._format_text(text)
        words = self._get_words(text)
        profanities = self._check_profanities(words)
        return profanities
