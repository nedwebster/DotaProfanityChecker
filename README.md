# DotaProfanityChecker
Small package to check curse words in a given dota2 match. The code pulls game info from the https://api.opendota.com/api/ for a given match_id. Once the game is loaded, the Game class has specific methods to analyse the text in the replay.

## Warning!
lookups/curse_words.txt contains a large collection of curse words that some readers might find offensive.

## Example
```
import dota_profanity_checker

MATCH_ID = 3721302106
game_parser = dota_profanity_checker.GameParser(MATCH_ID)

game_parser.profanity_check()
```