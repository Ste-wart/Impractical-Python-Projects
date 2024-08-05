"""ETAOIN, by Stewart Magnus Simon stewartmagnus@gmail.com.

The six most commonly used letters in the English language can be remembered
with the mnemonic “etaoin” (pronounced eh-tay-oh-in). Write a Python
script that takes a sentence (string) as input and returns a simple bar chart–
type display.
"""

from collections import defaultdict
import pprint

alpha = 'abcdefghijklmnopqrstuvwxyz'
eta = defaultdict(list)


def main() -> None:
    """Map letters from string into dictionary & print bar chart of frequency."""
    res = input('Enter your sentence here: > ').lower()
    sentence = res.replace(' ', '')

    for i in alpha:
        eta[i].clear()

    for letter in sentence:
        if letter.isalpha():
            eta[letter].append(letter)
    print()
    pprint.pprint(eta)


if __name__ == '__main__':
    main()

text = 'Like the castle in its corner in a medieval game, I forsee terrible trouble and i stay here just the same.'
text_spanish = ('Como el castillo en su esquina en un juego medieval, preveo problemas terribles y de todos modos me '
                'quedo aquí.')
text_french = ('Comme le château dans son coin dans un jeu médiéval, je prévois de terribles ennuis et je reste ici '
               'quand même.')
