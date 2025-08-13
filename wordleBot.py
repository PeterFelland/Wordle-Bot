from wordleBotFunctions import score
from wordleBotFunctions import uniqueWord


orig_freq_dict = {
    'a': 7128,
    'b': 1849,
    'c': 2246,
    'd': 2735,
    'e': 7455,
    'f': 1240,
    'g': 1864,
    'h': 1993,
    'i': 4381,
    'j': 342,
    'k': 1753,
    'l': 3780,
    'm': 2414,
    'n': 3478,
    'o': 5212,
    'p': 2436,
    'q': 145,
    'r': 4714,
    's': 7319,
    't': 3707,
    'u': 2927,
    'v': 801,
    'w': 1127,
    'x': 326,
    'y': 2400,
    'z': 503
}

# Initally run to calculate the above values. No need to run on every iteration.
# with open('words.txt', 'r') as file:
#     for line in file:
#         line = line.strip()
#         for c in line:
#             freq_dict[c] += 1
# print(freq_dict)

#Score 5 letter words. Could only be run once and then modify the original txt file, but leaving this in case the scoring criteria changes.
scored_words = {}
with open('words.txt', 'r') as file:
    for line in file:
        line = line.strip()
        curScore = score(line, orig_freq_dict)
        scored_words[line] = curScore

# Print top COUNTER words, with optional conditions.
# counter = 0
# for k, v in sorted(scored_words.items(), key=lambda p:p[1], reverse=True):
#     if(uniqueWord(k)):
#         counter += 1
#         print(k,v)
#     if(counter == 20):
#         break


#Guess best word - highest letter frequency score
# Top 3 words with 5 unique letters are:
# soare 31828
# arose 31828
# aeros 31828
# I select to use SOARE or AROSE as the start word
seedWord = "SOARE"
botGuess = seedWord.lower()
numberOfGuesses = 1
pastGuesses = [botGuess]
guessHistory = []

# Possible letters for each 'digit'
correctLetters = [
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
]

print("I guess '" + seedWord + "' as my first guess")
print("Please enter G for green, Y for yellow, and B for black for corresponding correctness: ")
guess = input().lower()


while(numberOfGuesses < 6 and guess != 'ggggg'):
    guessHistory.append(guess)
    mustContain = []
    possibleGuesses = []
    #Update correct letters for each slot in the word based on correctness input
    for i, c in enumerate(guess):
        if(c == 'g'):
            # If green, correctLetters only has one option for that slot. It also must contain that letter.
            correctLetters[i] = [botGuess[i]]
            mustContain.append(botGuess[i])
        elif(c == 'y'):
            # If yellow, the letter must be removed from the current slot and the word must contain that letter.
            charIndex = 0
            for ind, char in enumerate(correctLetters[i]):
                if(char == botGuess[i]):
                    charIndex = ind
                    break
            del correctLetters[i][charIndex]
            mustContain.append(botGuess[i])
        else:
            # If black, remove the letter from all slots.
            for slot in correctLetters:
                if(len(slot) > 1):
                    for ind, char in enumerate(slot):
                        if(char == botGuess[i]):
                            del slot[ind]
                            break
    # Iterate through the scored words in reverse order. The lowest index has the highest score, which makes it the 'best' guess given no other criteria.
    # Check if the letters in the current word match the available letters in correctLetters.
    for k, v in sorted(scored_words.items(), key=lambda p:p[1], reverse=True):
        if(k[0] in correctLetters[0] and k[1] in correctLetters[1] and k[2] in correctLetters[2] and k[3] in correctLetters[3] and k[4] in correctLetters[4]):
            # After redoing some of the above filtering logic, this section appears to be deprecated. Still testing. Must contain is an array, not a set.
            # Boolean array that indicates if a slot in the word has been checked. This is to account for words with duplicate letters.
            # checked = [False, False, False, False, False]
            # trueChecked = 0
            # for char in mustContain:
            #     for i in range(len(k)):
            #         if(char == k[i] and checked[i] == False):
            #             checked[i] = True
            #             trueChecked += 1
            #             break
            # #Possible guesses have an equal number of slots checked as the length of what the word must contain, as that is what has been confirmed from the input. 
            # if(trueChecked == len(mustContain)):
            #     print(k, v)
            #     possibleGuesses.append(k)
            possibleGuesses.append(k)
    # print(possibleGuesses)
    # Prioritize unique lettered words for guesses 2-5
    uniqueGuess = False
    if(numberOfGuesses < 5):
        for word in possibleGuesses:
            if(uniqueWord(word)):
                botGuess = word
                uniqueGuess = True
                break
    if not uniqueGuess:
        botGuess = possibleGuesses[0]
    print(possibleGuesses)
    pastGuesses.append(botGuess)
    # print(pastGuesses)
    print(mustContain)
                
    numberOfGuesses += 1
    print("Guess #" + str(numberOfGuesses) + ": " + botGuess)
    guess = input()

# Prints out the guesses made and green/yellow/black square emojis if set to True
emojiOutput = True

if(guess == 'ggggg'):
    print("I won in " + str(numberOfGuesses) + " guesses!")
    if emojiOutput:
        guesses = ""
        for guess in pastGuesses:
            guesses += guess + " -> "
        print("Bot Guesses: ||" + guesses[:-4] + "||")
        
        guessHistory.append('ggggg')
        for guess in guessHistory:
            output = ''
            for c in guess:
                if c == 'g':
                    output += ":green_square:"
                elif c == 'y':
                    output += ":yellow_square:"
                else:
                    output += ":black_large_square:"
            print(output)
        
else:
    print("I did not get the answer =(")