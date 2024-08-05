"""ETAOIN, by Stewart Magnus Simon stewartmagnus@gmail.com.

The six most commonly used letters in the English language can be remembered
with the mnemonic “etaoin” (pronounced eh-tay-oh-in). Write a Python
script that takes a sentence (string) as input and returns a simple bar chart–
type display.
"""

from collections import defaultdict
import pprint

eta = defaultdict(list)


def main() -> None:
    """Map letters from string into dictionary & print bar chart of frequency."""
    res = input('Enter your sentence here: > ').lower()
    sentence = res.replace(' ', '')

    for letter in sentence:
        if letter.isalpha():
            eta[letter].append(letter)
    print()
    pprint.pprint(eta)


if __name__ == '__main__':
    main()
