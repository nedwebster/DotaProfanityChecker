import string


class ChatParser:
    """Class for handling the parsing and formatting of chat values."""

    PUNCTUATION = set(string.punctuation)

    @classmethod
    def _remove_punctuation(cls, text: str) -> str:
        """Removes punctuation from text."""

        return "".join(x for x in text if x not in cls.PUNCTUATION)

    @classmethod
    def _get_words_list(cls, text: str) -> list:
        """Splits a formatted text string into a list of seperate words."""
        for ch in text:
            if ch in cls.PUNCTUATION:
                raise ValueError(
                    "text contains punctuation, clean before generating words"
                )
        return text.split(" ")

    def format_text(self, text: str) -> str:
        """Format text. Converts to lower case, then removes punctuation."""

        lower_case_text = text.lower()
        lower_case_words = self._remove_punctuation(lower_case_text)
        list_of_words = self._get_words_list(lower_case_words)

        return list_of_words
