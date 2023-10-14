"""
Anagram
Write a function check_anagram(word_1, word_2) which takes two strings
and checks whether these words are an anagram.
Upper and lower case should be ignored.

An anagram is a sequence of letters that is formed from another sequence of letters 
simply by rearranging the letters.

Return value: Boolean
Example: Life - File

The word pairs to be compared are available as a list of tuples:

wordlist = [
    ('Leben', 'Nebel'),
    ('Sinn', 'nins'),
    ('auto', 'baum')
    ]

Call check_anagram iteratively for each element of wordlist.
"""
wordlist = [
    ('Leben', 'Nebel'),
    ('Sinn', 'nins'),
    ('auto', 'baum')
    ]


def check_anagram(word1, word2):
    if "".join(sorted(word1.lower())) == "".join(sorted(word2.lower())):
        return True
 
    return False
 
 
wordlist = [
    ('Leben', 'Nebel'),
    ('Sinn', 'nins'),
    ('auto', 'baum')
]
 
for w1, w2 in wordlist:
    print(check_anagram(w1, w2))
