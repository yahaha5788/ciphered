from string import ascii_lowercase
from typing import Final

base_list: Final[list[str]] = list(ascii_lowercase)

def _shift(letter: str, shift: int) -> str:
    """
    Shifts a given letter over by <shift> spaces in the English alphabet.
    :param letter: The given letter
    :param shift: The number of spaces to shift the letter over by
    :return: The shifted letter.
    """
    letter_index = base_list.index(letter)
    letter_index += shift
    if not letter_index < 26:
        letter_index -= 26

    return base_list[letter_index]

def _is_in_alphabet(char):
    if char not in base_list:
        return False
    else:
        return True

def caesar_cipher(plaintext: str, shift: int) -> str:
    """
    Shifts a given phrase over by ``shift`` spaces in the alphabet
    :param plaintext: The plaintext phrase to shift over
    :param shift: The amount of spaces to shift it over by
    :return: The ciphertext.
    """
    ciphertext: str = ""
    for i in list(plaintext.lower()):
        if _is_in_alphabet(i):
            ciphertext += _shift(i, shift)
        else:
            ciphertext += i

    return ciphertext

def brute_force(ciphertext: str) -> dict[int, str]:
    iterations: dict[int, str] = {}
    for shift in range(1, 26):
        iterations[shift] = caesar_cipher(ciphertext, shift)

    return iterations