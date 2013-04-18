import pylab
import string

def loadWords(wordFile):
    print "Loading word list {0}.".format(wordFile)

    inFile = open(wordFile, 'r', 0)

    if wordFile == 'ps3_words.txt':
        line = inFile.readline()
        wordList = line.split()
    elif wordFile == 'ps4_words.txt':
        wordList = []
        for line in inFile:
            wordList.append(line.strip().lower())
    else:
        raise "Unknown word list: {0}".format(wordFile)

    print "{0} words loaded from {1}".format(len(wordList), wordFile)

    return wordList

def getFirstLetters(wordList):
    firstLetter = []
    for word in wordList:
        firstLetter.append(word[0])

    return firstLetter

def getWordLengths(wordList):
    wordLength = []
    for word in wordList:
        wordLength.append(len(word))

    return wordLength

def getLetterCounts(letterList):
    letters = {}
    for letter in letterList:
        letters[letter] = letters.get(letter, 0) + 1

    for alphabet in string.lowercase:
        if letters.get(alphabet, 0) == 0:
            letters[alphabet] = 0

    return letters

def getLetterProportions(letterDict):
    total = 0.0
    for key in letterDict:
        total += letterDict[key]

    proportions = {}
    for key in letterDict:
        proportions[key] = letterDict[key] / total

    return proportions

def dictionaryToLists(dictionary1, dictionary2):
    proportions1 = []
    proportions2 = []
    letters = []

    for key in dictionary1:
        proportions1.append(dictionary1[key])
        proportions2.append(dictionary2[key])
        letters.append(key)

    return (proportions1, proportions2, letters)

def plotFirstLetterProportions(ps3, ps4, letters):
    pylab.figure(1)
    pylab.plot(ps3, ps4, 'w.', alpha=0.0)
    pylab.title('Proportions of Words Starting With Each Letter')
    pylab.xlabel('Proportions of Problem Set 3 Word List')
    pylab.ylabel('Proportions of Problem Set 4 Word List')

    for i in range(len(letters)):
        pylab.annotate(letters[i], (ps3[i], ps4[i]), color='b')

    pylab.show()



ps3_words = loadWords('ps3_words.txt')
ps3_lengths = getWordLengths(ps3_words)
ps3_firstletters = getFirstLetters(ps3_words)
ps3_firstLetterCounts = getLetterCounts(ps3_firstletters)
ps3_firstLetterProportions = getLetterProportions(ps3_firstLetterCounts)

ps4_words = loadWords('ps4_words.txt')
ps4_lengths = getWordLengths(ps4_words)
ps4_firstletters = getFirstLetters(ps4_words)
ps4_firstLetterCounts = getLetterCounts(ps4_firstletters)
ps4_firstLetterProportions = getLetterProportions(ps4_firstLetterCounts)

ps3Props, ps4Props, letters = dictionaryToLists(ps3_firstLetterProportions,
        ps4_firstLetterProportions)
plotFirstLetterProportions(ps3Props, ps4Props, letters)

print "3: Max word length - {0}, min word length - {1}".format(
        max(ps3_lengths), min(ps3_lengths))
print "4: Max word length - {0}, min word length - {1}".format(
        max(ps4_lengths), min(ps4_lengths))

print "3: First letters - {0}".format(ps3_firstLetterCounts)
print "4: First letters - {0}".format(ps4_firstLetterCounts)
print "3: First letter proportions - {0}".format(ps3_firstLetterProportions)
print "4: First letter proportions - {0}".format(ps4_firstLetterProportions)

print
print "3: Proportions as lists - {0}".format(ps3_kv)
