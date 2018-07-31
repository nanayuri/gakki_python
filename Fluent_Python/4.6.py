from unicodedata import normalize
from unicodedata import combining
import string


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()


def shave_marks(txt):
    norm_txt = normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not combining(c))
    return normalize('NFC', shaved)


def shave_marks_latin(txt):
    norm_txt = normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if combining(c) and latin_base:
            continue
        keepers.append(c)
        if not combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return normalize('NFC', shaved)