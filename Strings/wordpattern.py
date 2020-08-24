from collections import defaultdict


def wordpattern(pattern, str):
    word = str.split()
    if len(word) != len(pattern):
        return False

    letterToWord, wordToLetter = defaultdict(), defaultdict()
    for i in range(len(pattern)):
        letter, pattern = pattern[i], word[i]
        letterToWord.setdefault(letter, word)
        wordToLetter.setdefault(word, letter)

        if letterToWord[letter] != word or wordToLetter[word] != letter:
            return False
    return True


