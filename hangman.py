import random

from words import word_list

def get_word():
    word = random.choice(word_list)
    # return random word in all uppercase, convert all user input to uppercase to make comparison logic simpler
    return word.upper()

# create variables updating for each turn user takes
# display word for each turn
def play(word):
    word_completion = "_" * len(word)
    # guessed variable initialised to false
    guessed = False
    guessed_letters = []
    guessed_words = []
    # bodyparts left to be drawn
    tries = 6
    print("Let's play Hangman!")
    # print initial stage of hangman
    print(display-hangman(tries))
    # initial stage of word with all underscores
    print(word_completion)
    print("\n")
    # while loop to get tries
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        # guess letter, word or typing other than single letter or word of correct length
        if len(guess) == 1 and guess.isalpha():
            # conditional block to see if letter already guessed, not in word or is in words
            if guess in guessed_letters:
                print("You already guessed the letter", guess) #guess is print the letter
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job," guess, "is in the word!")
                guessed_letters.append(guess)
                # update word completion for all occurences of guess
                # convert word completion from string to list to index into it, store in new variable: word_as_list
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess)
                for index in indices:
                    word_as_list[index] = guess
                # index guess letters into word
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word!," guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        # print new line to space out each term
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("You guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def main():
    word = get_word()
    play(word)
    while input("Play again (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

# make sure it runs on the command line
if __name__ == "__main__":
    main()
