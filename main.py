from profanity import ProfanityChecker
from loader import Loader


MATCH_ID = 3721302106


if __name__ == "__main__":

    my_game = Loader().load_match(match_id=MATCH_ID)

    my_game.profanity_check()
