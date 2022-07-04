from word import words # word is a py file of letters
import random
import string


def get_valid_word(words):
    word = random.choice(words)  # selecting a word from list
    while '-' in word or ' ' in word:  # if word contain either keep searching for a new word
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)  # letter in for words
    # list of uppercase letter in dictionary
    alphabet = set(string.ascii_uppercase)
    used_letter = set()  # words usser has guessed
    lives = 6
    while len(word_letter) > 0 and lives > 0:
        print(f' You have {lives} remaing. Letters you have already used are: ', " ".join(
            used_letter))
        word_list = [
            letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Enter the words: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives -= 1
                print('User letter is not in the word')

        elif user_letter in used_letter:
            print('You have already used The letter')

        else:
            print("Wrong character")
    if lives == 0:
        print(f'You have died. The word was: {word}')
    else:
        print(f'You have gussed the word correctly: {word}')


hangman()
