"""Anagram Phrase, by Stewart Magnus Simon."""

import sys
from collections import Counter
from load_dictionary import load

dict_file = load('words.txt')
dict_file = sorted(dict_file)

init_name = input('Enter a name :> ')


def find_anagrams(name: str, word_list: list[str]) -> None:
    """Read name & dictionary file & displays all anagrams IN name.

    :param name: (str):
    :param word_list: (list[str]):
    :return: None
    """
    name_count = Counter(name)
    anagrams = []

    for word in word_list:
        test = ''
        word_count = Counter(word.lower())
        for letter in word:
            if word_count[letter] <= name_count[letter]:
                test += letter

        if Counter(test) == word_count:
            anagrams.append(word)

    print(*anagrams, sep='\n')
    print()
    print(f'Remaining letters = {name}')
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")


def process_choice(name: str) -> tuple[str, str]:
    """Check user choice for validity, return choice and leftover letters.

    :param name:
    :return:
    """
    while True:
        choice = input('\nMake a choice else Enter to start over or # to end :> ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()

        candidate = ''.join(choice.lower().split())
        left_over = list(name)
        for letter in candidate:
            if letter in left_over:
                left_over.remove(letter)
        if len(name) - len(left_over) == len(candidate):
            break
        print("Won't work! Make another choice!", file=sys.stderr)

    name = ''.join(left_over)  # makes display more readable.
    return choice, name


def main():
    """Help user build anagram phrase from their name."""
    name = ''.join(init_name.lower().split())  # To avoid space in the name.
    name = name.replace('-', '')
    limit = len(name)
    running = True
    phrase = ''

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f'Length of anagram phrase = {len(temp_phrase)}')

            find_anagrams(name, dict_file)
            print('Current anagram phrase =', end='')
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print('\n*****FINISHED!!!*****\n')
            print(phrase, file=sys.stderr)
            print()

            try_again = input('\nTry again? (Press Enter else "n" to quit)\n')
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
