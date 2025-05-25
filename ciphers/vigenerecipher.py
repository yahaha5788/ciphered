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

def _decode(grid: list[list[str]], cipher_letter: str, key_letter: str) -> str:

    row = next(row for row in grid if row[0] == key_letter)
    ind = row.index(cipher_letter)

    return base_list[ind]


# --------------------------- USE THIS --------------------------- #
def vigenere_cipher(plain_or_ciphertext: str, keyword: str, encode: bool = True) -> str:
    """
    The actual cipher function which uses all the other functions
    :param encode: True by default to encode, set False to decode text
    :param plain_or_ciphertext: the plaintext to encode
    :param keyword: the keyword to use
    :return: the ciphertext
    """
    grid = _generate_grid()

    p_or_c: list[str] = list(plain_or_ciphertext.lower())
    keyword = list(keyword.lower())

    result_text = ""
    key_index = 0

    for char in p_or_c:
        if char in ascii_lowercase:

            key_char = keyword[key_index % len(keyword)]

            if encode:
                result_text += _encode(grid, char, key_char)
            else:
                result_text += _decode(grid, char, key_char)

            key_index += 1
        else:
            result_text += char

    return result_text