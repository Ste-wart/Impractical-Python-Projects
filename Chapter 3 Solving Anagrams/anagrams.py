"""Anagram, by Stewart Magnus Simon (stewartmagnus2001@gmail.com)."""

from load_dictionary import load

word_list = load('words.txt')


def main() -> None:
    """Interactive shell for Anagram finder.

    :return: None
    """
    print('Welcome to Anagram finder')

    # Input a SINGLE word below to find its anagram(s):
    word = input('Please Enter your word :> ').lower()
    print(f'Input name = {word.title()}')
    print(f'Using name: {word}\n')
    anagram_list = anagram(word.strip())

    # Print out list of anagrams.
    if len(anagram_list) == 0:
        print('You need a larger dictionary or a new name!')
    elif len(anagram_list) == 1:
        print('1 Anagram found =', *anagram_list)
    else:
        print(f'{len(anagram_list)} Anagrams found =', *anagram_list, sep='\n')


def anagram(word: str) -> list:
    """Anagram finder algorithm.

    :param word: (str): Word to search its anagrams.
    :return: (list): A list of found anagrams.
    """
    anagram_list = []
    # sort name and find anagrams
    s_word = sorted(word)
    for wor in word_list:
        wor = wor.lower()
        if wor != word:
            if sorted(wor) == s_word:
                anagram_list.append(wor)
    return anagram_list


if __name__ == '__main__':
    main()
