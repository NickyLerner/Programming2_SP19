import random
done = False
game_over = False
answer = False
print("TIME FOR SOME HANGMAN!\n")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1 ----- I did not do this
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game --- thanks for this
word_list = ["CARRION", "QUINCE", "FACADE", "ROWDY", "DROW", "BRICK", "PANDA", "KABOOM", "OTTER"]
guessed_letters = []
misses = 0
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = word_list[random.randrange(len(word_list))]
spaces = []
guessed_word = ""
for i in range(len(word)):
    spaces.append("_")

while not done:

    for letters in spaces:
        print(letters, end=" ")

    print()

    for letters in guessed_letters:
        print(letters + ",", end=" ")

    print()
    current_letter = input("\nWhat letter do you guess?").upper()

    if current_letter in guessed_letters:
        print("You already guessed that letter.")

    elif current_letter.lower() in alphabet:
        guessed_letters.append(current_letter)

        if current_letter in word:
            print(HANGMANPICS[misses])

            for i in range(len(word)):
                if current_letter == word[i]:
                    spaces[i] = current_letter

            for letters in spaces:
                guessed_word += letters
                guessed_word = guessed_word[-len(word):]

            if guessed_word[-len(word):] == word:
                game_over = True
                answer = True
                print("\nYou Win!")

        else:
            misses += 1
            print(HANGMANPICS[misses])
            print("That is", misses, "misses. You have", 6 - misses, "left.")
            if misses == 6:
                game_over = True
                answer = True
                print("Game Over")

    else:
        print("That's not a letter.")

    while game_over:
        if answer:
            misses = 0
            print(word)
            answer = False
        keep_going = input("\nDo you want to play again?    (y/n)")

        if keep_going == "y":
            game_over = False
            guessed_letters = []
            word = word_list[random.randrange(len(word_list))]
            spaces = []
            guessed_word = ""
            for i in range(len(word)):
                spaces.append("_")
            print("\n\n\n\n\n\nTIME FOR SOME HANGMAN!")

        if keep_going == "n":
            done = True
            game_over = False

    print()
print("Goodbye.")
