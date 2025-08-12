A program that attempts to solve the daily wordle.
It uses a seed word that was originally calculated based on the frequency of letters, with "Soare," "Arose," and "Aeros" having the highest score with 5 unique letters. This seed word can be changed, though, to whatever the user desires.
Upon making the first guess, user input is required to validate the accuracy of the guess. User input is 5 characters long and consists of a 'b', 'y', or 'g'
- 'b' represents a black letter; one that is not in the solution
- 'y' represents a yellow letter; one that is in the solution, but in the wrong place
- 'g' represents a green letter; one that is in the correct space
The bot will keep guessing until 6 guesses are made, or it gets the solution as confirmed by 'ggggg' user input. 
