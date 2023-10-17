import pytest
from myfirstpackage.snowman import choose_word, display, game  # Replace 'your_module' with the actual name of your Python script

# Mocking random.choice to control its output
from unittest.mock import patch

# Test the choose_word function
def test_choose_word_default():
    with patch('random.choice', return_value='apple'):
        assert choose_word() == 'apple'

def test_choose_word_custom_list():
    with patch('random.choice', return_value='custom_word'):
        assert choose_word(["custom_word"]) == 'custom_word'

def test_choose_word_empty_list():
    with pytest.raises(IndexError):
        choose_word([])

# Test the display function
def test_display_full_guesses():
    assert display("apple", "apple") == "apple"

def test_display_partial_guesses():
    assert display("apple", "apl") == "appl_"

def test_display_no_guesses():
    assert display("apple", "") == "_____"

# Test the game function
def test_game_win():
    with patch('random.choice', return_value='apple'):
        assert game(guess_list=['a', 'p', 'l', 'e']) == ["You've guessed the word: apple"]

def test_game_lose():
    with patch('random.choice', return_value='apple'):
        assert game(guess_list=['x', 'y', 'z', 'a', 'b', 'c','d']) == ["Game over"]

def test_game_partial_guesses():
    with patch('random.choice', return_value='apple'):
        assert game(guess_list=['a', 'p']) == []

def test_game_custom_word_list():
    with patch('random.choice', return_value='custom_word'):
        assert game(word_list=['custom_word'], guess_list=['c', 'u', 's', 't', 'o', 'm', '_', 'w', 'o', 'r', 'd']) == ["You've guessed the word: custom_word"]
