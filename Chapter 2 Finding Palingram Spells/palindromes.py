"""Find palindromes in a dictionary file."""

from load_dictionary import load

word_list = load('words.txt')

pali = [word for word in word_list
        if len(word) > 1 and word[::-1] == word]

print(f'\nNumber of Palindromes found = {len(pali)}')
print(*pali, sep='\n')
