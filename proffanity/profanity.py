import string as s


class ProfanityChecker:

    def __init__(self):

        def load_profanity_list():
            """Loads the curse words from the local text file."""
            with open("curse_words.txt", "r") as f:
                return f.read()

        def format_profanity_list(profanity_list: str) -> list:

            return profanity_list.split("\n")

        profanity_list = load_profanity_list()
        self.profanity_list = format_profanity_list(profanity_list)

    def _format_profanity_list(profanity_list: str) -> list:

        return profanity_list.split("\n")

    @staticmethod
    def _format_string(string):
        string = string.lower()
        exclude = set(s.punctuation)

        return "".join(x for x in string if x not in exclude)

    @staticmethod
    def _word_count(string, word):
        words = string.split(" ")

        return words.count(word)


if __name__ == "__main__":

    prof_checker = ProfanityChecker()

    x = "Hello my name is Ned"
    print(prof_checker(x))
