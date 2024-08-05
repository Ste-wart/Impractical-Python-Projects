"""Find palindromes in a dictionary file."""

from load_dictionary import load

word_list = load('words.txt')


def pali_rec(wor):
    pali = []
    if wor == '' or len(wor) == 1:
        pali.append(wor)
    elif wor[0] == wor[-1]:
        pali_rec(wor[1:-1])
        pali.append(wor)

    return pali


a = pali_rec('popop')
print(a)

# print(f'\nNumber of Palindromes found = {len(pali)}')
# print(*pali, sep='\n')

range()
