from string import ascii_lowercase
from typing import Final

base_list: Final[list[str]] = list(ascii_lowercase)

def _generate_grid() -> list[list[str]]:
    """
    Creates the 26x26 grid of letters used in a vigenere cipher.
    The "grid" is a list of lists of the alphabet, shifted over.
    :return: the grid
    """
    row = list(ascii_lowercase)

    grid: list[list[str]] = [base_list]

    for x in range(1, 26):
        new_row = row.copy()
        letter = new_row[0]
        new_row.pop(0)
        new_row.append(letter)
        grid.append(new_row)
        last_row = new_row
        row = last_row

    return grid

def _fix_key(desired_index: int, key: list[str]) -> list[str]:
    """
    trims the given keyword to the length of the plaintext.
    :param desired_index: the length of the plaintext
    :param key: the keyword
    :return: the fixed key
    """
    result_key = key.copy()

    while len(result_key) < desired_index:
        result_key += key

    while len(result_key) > desired_index:
        result_key.pop(len(result_key)-1)

    return result_key

def _encode(grid: list[list[str]], plain_letter: str, key_letter: str) -> str:
    """
    encodes a given letter using the grid and a corresponding key letter
    :param grid: the grid to use
    :param plain_letter: the letter to encode
    :param key_letter: the corresponding keyword letter
    :return: the encoded letter
    """
    plain_index = base_list.index(plain_letter)
    key_index = base_list.index(key_letter)

    return grid[plain_index][key_index]


# --------------------------- USE THIS --------------------------- #
def vigenere_cipher(plaintext: str, keyword: str) -> str:
    """
    The actual cipher function which uses all the other functions
    :param plaintext: the plaintext to encode
    :param keyword: the keyword to use
    :return: the ciphertext
    """
    grid = _generate_grid()

    plaintext: list[str] = list(plaintext.lower())
    keyword: list[str] = _fix_key(len(plaintext), list(keyword.lower()))

    cipher_letters = list(zip(plaintext, keyword))
    for t in cipher_letters:
        if t[0] not in base_list:
            ind = cipher_letters.index(t)
            keyword.insert(ind, " ")

    cipher_letters = list(zip(plaintext, keyword))
    ciphertext = ""

    for i in cipher_letters:
        if i[0] in base_list:
            ciphertext += _encode(grid, i[0], i[1])
            print('base')
        else:
            ciphertext += i[0]
            print('not base')

    return ciphertext

