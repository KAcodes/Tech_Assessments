"""Tests for coding problems"""
from assessment import calculate_points_for_word, calculate_point, distribute_letters_to_player

def test_word_guardian():
    assert calculate_points_for_word("GUARDIAN") == 10


def test_empty_word():
    assert calculate_points_for_word("") == 0


def test_calculate_letter_g():
    assert calculate_point("G") == 2


def test_calculate_letter_z():
    assert calculate_point("z") == 7


def test_letters_distributed():
    assert len(distribute_letters_to_player()) == 7
    