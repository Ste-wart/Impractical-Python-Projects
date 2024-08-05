"""Finding Voldemort: The British Brute-Force, by Stewart Magnus Simon.

Reduce the number of anagrams of tmvoordle to a manageable number that will still contain
Voldemort.
"""

import sys
from itertools import permutations
from collections import Counter
from load_dictionary import load

word_list_init = load('2of4brif.txt')
trigrams = load('least-likely_trigrams.txt')
VOWELS = 'aeiouy'
REJECTS = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
           'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
FIRST_PAIR_REJECTS = ['ld', 'lm', 'lt', 'lv', 'rd',
                      'rl', 'rm', 'rt', 'rv', 'tl', 'tm']

# Use ANSI codes to change the text color
RED = "\033[31m"
RESET = "\033[0m"


def main() -> None:
    """Load files, run filters, allow user to view anagrams by 1st letter.

    :returns: None
    """
    name = 'tmvoordle'.lower()
    word_list = prep_words(name, set(word_list_init))

    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams)
    filter_3 = letter_pair_filter(filter_2)

    view_by_letter(name, filter_3)


def prep_words(name: str, word_list: set[str]) -> set[str]:
    """Prep word list for finding anagrams.

    :param name: (str): Word to use in the program.
    :param word_list: Set of dictionary words.
    :return: (set[str]): Set of dictionary words excluding words equal in length with name.
    """
    print(f'length initial word_list = {len(word_list)}')
    nl = len(name)

    new_word_list = {word.lower() for word in word_list
                     if len(word) == nl}
    # To track how much impact the filters are having on the list.
    print(f'Length of new word_list = {len(new_word_list)}')
    return new_word_list


def cv_map_words(word_list: set[str]) -> set[str]:
    """Map letters in words to consonants & vowels.

    :param word_list: Set of words.
    :return: Set of consonants-vowels mappings
    """
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in VOWELS:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)

    # determine number of UNIQUE c - v patterns:
    total = len(set(cv_mapped_words))
    # target fraction to eliminate.
    target = 0.05
    # get number of items in target fraction
    n = int(total * target)

    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = {pattern for pattern, _ in count_pruned}

    print(f'Length filtered_cv_map = {len(filtered_cv_map)}')
    return filtered_cv_map


def cv_map_filter(name: str, filtered_cv_map: set[str]):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    # Using sets for efficiency and to remove duplicates.
    perms = {''.join(i) for i in permutations(name)}
    print(f'length of initial permutations set = {len(perms)}')

    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in VOWELS:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)

    print(f'# choices after filter_1 = {len(filter_1)}')
    return filter_1


def trigram_filter(filter_1: set[str], trigram: list[str]) -> set[str]:
    """Remove unlikely trigrams from permutations."""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigram:
            if triplet.lower() in candidate:
                filtered.add(candidate)

    # filtered = {candidate for triplet in trigram
    #             for candidate in filter_1
    #             if triplet.lower() in candidate}

    filter_2 = filter_1 - filtered
    print(f'# Choices after filter_2 = {len(filter_2)}')
    return filter_2


def letter_pair_filter(filter_2: set[str]) -> set[str]:
    """Remove unlikely letter-pairs from permutations."""
    filtered = set()

    for candidate in filter_2:
        for r in REJECTS:
            if r in candidate:
                filtered.add(candidate)
        for fp in FIRST_PAIR_REJECTS:
            if candidate.startswith(fp):
                filtered.add(candidate)

    filter_3 = filter_2 - filtered
    print(f'# choices after filter_3 = {len(filter_3)}')

    if 'voldemort' in filter_3:
        print(f'{RED}Voldemort found!{RESET}')
    return filter_3


def view_by_letter(name: str, filter_3: set[str]) -> None:
    """Filter to anagrams starting with input letter."""
    print(f'Remaining letters = {name}')
    first = input('select a starting letter or press Enter to see all :> ')

    subset = [candidate for candidate in filter_3 if candidate.startswith(first)]
    subset.sort()

    print(*subset, sep='\n')
    print(f'Number of choices starting with {first} = {len(subset)}')
    try_again = input('Try again? (Press Enter else any other key to EXIT) :> ')
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        print('Thanks!!!')
        sys.exit()


if __name__ == '__main__':
    main()
