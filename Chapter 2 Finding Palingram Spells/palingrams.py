"""Find all word-pair palingrams in a dictionary file."""

from load_dictionary import load

word_list = load('2of4brif.txt')


# Find word-pair palingrams.
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list


palingrams = find_palingrams()
palingrams.sort()  # sort palingrams on first word.

# display list of palingrams.
print(f'\nNumber of palingrams found = {len(palingrams)}\n')
for first, second in palingrams:
    print(f'{first} {second}')
