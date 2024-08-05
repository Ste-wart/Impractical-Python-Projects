"""Pig Latin, by Stewart Magnus Simon stewartmagnus@gmail.com.

To form Pig Latin, you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the
word.
"""

VOWELS = tuple('aeiou')
VO = 'way'
CO = 'ay'

NOTE = """Pig Latin, by Stewart Magnus Simon stewartmagnus@gmail.com

To form Pig Latin, you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the
word."""


def main() -> None:
    """Create your very own Pig Latin Phrase.

    :return: None
    """
    print(NOTE)
    print('\nENTER `quit` to leave the program')
    while True:
        res = input('Enter your sentence here: > ')

        if res.lower() == 'quit':
            break

        phrase = res.split()
        latin_phrase = latin_comp(phrase)
        print(' '.join(latin_phrase))
        print()


def latin(phrase: list) -> list:
    """Take a list of English strings and transforms it into Pig latin.

    :param phrase: list of English strings.
    :return: list of Pig Latin strings.
    """
    new_sen = []
    for word in phrase:
        if word.startswith(VOWELS):
            word += VO
            new_sen.append(word.lower())
        else:
            q = word[0]
            s = word[1:]
            s += q + CO
            new_sen.append(s.lower())

    return new_sen


def latin_comp(phrase: list) -> list:
    """Take a list of English strings and transforms it into Pig latin.

    :param phrase: list of English strings.
    :return: list of Pig Latin strings.
    """
    new_sen_comp = [(wor + VO).lower() if wor.startswith(VOWELS)
                    else (wor[1:] + wor[0] + CO).lower() for wor in phrase]

    return new_sen_comp


if __name__ == '__main__':
    main()
