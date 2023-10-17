import random
import pyfiglet

def choose_word(word_list=None):
    """
    choose_word function chooses a random word from a list of words

    Args:
        word_list (list, optional): List of words. Defaults to None.

    Returns:
        str: selected word
    """    
    if word_list is None:
        word_list = ["apple", "banana", "cherry", "date", "elderberry", "drexel"]
    return random.choice(word_list)

def display(word, guesses):
    """
    display displays the word

    Args:
        word (str): word
        guesses (str): guesses

    Returns:
        str: hidden string
    """
    return ''.join([char if char in guesses else '_' for char in word])

def game(word_list=None, guess_list=None):
    """
    game _summary_

    Args:
        word_list (_type_, optional): _description_. Defaults to None.
        guess_list (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    word = choose_word(word_list)
    attempts = 6
    guesses = []
    output = []

    for guess in guess_list:
        guesses.append(guess)
        if guess in word:
            if all([char in guesses for char in word]):
                output.append(f"You've guessed the word: {word}")
                break
        else:
            attempts -= 1

    if attempts == 0:
        output.append("Game over")

    return output
