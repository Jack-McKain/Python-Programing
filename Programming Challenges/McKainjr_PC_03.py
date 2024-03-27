import os
import doctest
from urllib.request import urlopen
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()
#print(words)


def allsteps(word):
    '''
    >>> allsteps("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']

    >>> allsteps("UC")
    ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']

    >>> allsteps("BEARCAT")
    ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']

    '''
    
    word = word.upper()
    valid_step_words = set()  # Avoid duplicates
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Create dictionary to speed up results
    words_dict = {}
    for w in words:
        sorted_w = ''.join(sorted(w))
        if sorted_w in words_dict:
            words_dict[sorted_w].append(w)
        else:
            words_dict[sorted_w] = [w]
    
    # Generate all possible step words
    for letter in alphabet:
        for i in range(len(word) + 1):
            # Insert the letter at every possible position
            new_word = word[:i] + letter + word[i:]
            sorted_new_word = ''.join(sorted(new_word))
            if sorted_new_word in words_dict:
                valid_step_words.update(words_dict[sorted_new_word])
    
    return sorted(list(valid_step_words))


if __name__ == "__main__":
  doctest.testmod(verbose=True)