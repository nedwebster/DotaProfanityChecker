# DotaProfanityChecker
Small package to check curse words in a given dota2 match. The code pulls game info from the https://api.opendota.com/api/ for a given match_id. Once the game is loaded, the Game class has specific methods to analyse the text in the replay.

## Example
```
import dota_profanity_checker

MATCH_ID = 3721302106
my_game = dota_profanity_checker.Loader().load_match(MATCH_ID)

my_game.profanity_check()
```