from random import choice
from string import ascii_uppercase


def random_string():
    return ''.join(choice(ascii_uppercase) for i in range(50))
