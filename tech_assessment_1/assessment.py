"""Technical assessment scrabble game"""
import string
import random

# Creating a letter-point distribution 

def calculate_point(letter: str) -> int:
    letter = letter.upper()
    one_point = ("EAIONRTLSU", 1)
    two_point = ("DG", 2)
    three_point = ("BCMP", 3)
    four_point = ("FHVWY", 4)
    five_point = ("K", 5)
    six_point = ("JX", 6)
    seven_point = ("QZ", 7)
    if letter in one_point[0]:
        return one_point[1]
    if letter in two_point[0]:
        return two_point[1]
    if letter in three_point[0]:
        return three_point[1]
    if letter in four_point[0]:
        return four_point[1]
    if letter in five_point[0]:
        return five_point[1]
    if letter in six_point[0]:
        return six_point[1]
    return seven_point[1]

def calculate_points_for_word(word: str) -> int:
    """Returns points for given input word"""
    # For each letter in word calculate point
    total = 0
    for letter in word:
        score = calculate_point(letter)
        total +=score
    # add this to a total word score 
    # And return
    return total



def add_letter()-> str:
    random_num = random.randint(0, 25)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[random_num]


def create_bag():
    bag = "EEEEEEEEEEEEAAAAAAAAAIIIIIIIIIOOOOOOOONNNNNNRRRRRRTTTTTTLLLLUUUUSSSSDDDDGGGBBCCMMPPFFHHVVWWYKJXQZ"
    return bag


def add_letter_bag():
    bag = create_bag()
    list
    chosen_letter = add_letter()
    
    pass

def distribute_letters_to_player() -> str:
    word = ""
    bag = list(create_bag())
    for num in range(7):
        letter = add_letter()
        if letter in bag:
            bag.remove(letter)
        word+= letter

    return word
