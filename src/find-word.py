#!/usr/bin/env python

import sys
import re

goodChars = r'[a-zA-Z ]'

def readfile(filename):
    file = open(filename, "r")
    filestr = file.read()
    file.close()
    return filestr

def filter(filestr):
    chars = list(filestr)

    newfilestr = ""

    for i in range(0, len(chars)):
        char = chars[i]
        valid = re.compile(goodChars)
        if not valid.match(char):
            chars[i] = " "
        newfilestr += chars[i]

    words = newfilestr.split()

    return words

def checkForWords(wordArr, word):
    timesFound = 0
    for i in range(len(wordArr)):
        wordArr[i] = wordArr[i].lower()
        word = word.lower()
        if wordArr[i] == word:
            timesFound += 1
        else:
            continue

    return timesFound

if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        word = sys.argv[2]

        readFilename = readfile(filename)
        filterFilename = filter(readFilename)
        checkWords = checkForWords(filterFilename, word)

        if checkWords > 0:
            times = "times" if checkWords > 1 else "time"
            print(f"\'{word}\' found in \'{filename}\' {checkWords} {times}")
        else:
            print(f"\'{word}\' not found in \'{filename}\'")
    else:
        print("Usage: ./find-word.py filename.txt word")
