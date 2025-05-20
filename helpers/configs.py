from enum import Enum

bg_color = "#1c1c1c"
fg_color = "#CFCFCF"
light_bg = "#272727"
grayed_out = "#5c5b5b"

cfg: dict = {
    'bg': '#272727',
    "borderwidth": '40',
    'relief': 'sunken',
    'width': '540',
    'height': '400'
}

main_cfg: dict = {
    'bg': bg_color,
    "borderwidth": '25',
    'relief': 'sunken',
    'width': '340',
    'height': '400'
}

desc_cfg: dict = {
    'bg': light_bg,
    'borderwidth': '25',
    'relief': 'sunken',
    'width': '200',
    'height': '400'
}

button_cfg: dict = {
    'bg': light_bg,
    'fg': fg_color,
    'borderwidth': '5',
    'relief': 'raised',
    'font': ('Calibri', 10)
}

entry_cfg: dict = {
    'bg': light_bg,
    'fg': fg_color,
    'font': ('Calibri', 10),
    'justify': 'left',
    'relief': 'groove',
    'bd': '3',
    'insertbackground': fg_color
}

label_cfg: dict = {
    'bg': bg_color,
    'fg': fg_color,
    'justify': 'left',
    'font': ('Calibri', 10),
}

class ButtonDescriptions(Enum):
    CAESAR = 'A caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet. For example, with a shift of 3, "A" becomes "D," "B" becomes "E," and so on. This is a form of monoalphabetic substitution, meaning each letter in the plaintext is consistently replaced by the same letter in the ciphertext'
    VIGENERE = "The Vigenère cipher is a method of encrypting alphabetic text using a series of interwoven Caesar ciphers based on a keyword. It's a polyalphabetic substitution cipher, meaning that different letters of the plaintext may be shifted by different amounts, depending on the keyword. This makes it more secure than monoalphabetic ciphers like the caesar cipher."