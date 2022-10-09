# guessing-game
Guessing Terminal Game Mini Project

1. Create a function that gets an integer, and it generates a random integer between 1 and that parameter.
2. Use `input` builtin function to guess the number and return True if the random and the guessed are equal
3. Create a function to introduce the following levels until you guess wrongly:
   1. Guess between 1 and 2; if correct then
   2. Guess between 1 and 4; if correct then
   3. Guess between 1 and 9; if correct then
   4. Guess between 1 and 16; if correct then you win!
4. Add "life" feature to the game. The player can guess wrong up to 3 times!
5. Modify the code to give as output the generated number in case of being wrong and print it
6. Modify the code to have 100 levels, but get a *life* whenever you are correct
7. Create a score function which starts from 0 and
   1. Adds `10 * "level"` for every correct answer
   2. Adds extra `100 * "consecutive correct answer"`
8. Create a function to save
   1. the highest score
   2. the average score
9. Modify the game to notify the player if he achieved a new high score and congratulate him if surpassed the average
