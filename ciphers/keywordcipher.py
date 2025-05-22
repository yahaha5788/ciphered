from string import ascii_lowercase
from typing import Final

base_list: Final[list[str]] = list(ascii_lowercase)


def _format_alphabet(keyword: list[str]) -> list[str]:
    keyword_alphabet: list[str] = base_list.copy()
    for n, k in enumerate(keyword):
        keyword_alphabet.pop(keyword_alphabet.index(k))
        keyword_alphabet.insert(n, k)

    return keyword_alphabet

def _encode(letter: str, keyword_alphabet: list[str]) -> str:
    ind = base_list.index(letter)
    return keyword_alphabet[ind]

def keyword_cipher(plaintext: str, keyword: str) -> str:
    plaintext: list[str] = list(plaintext.lower())
    keyword: list[str] = list(keyword.lower())
    keyword_alphabet = _format_alphabet(keyword)
    ciphertext = ""
    for p in plaintext:
        if p in base_list:
            ciphertext += _encode(p, keyword_alphabet)
        else:
            ciphertext += p

    return ciphertext