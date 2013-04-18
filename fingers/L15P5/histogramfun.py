import pylab


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = 'aeiou'
    vowelProportions = []

    for word in wordList:
        vowelsCount = 0.0

        for letter in word:
            if letter in vowels:
                vowelsCount += 1

        vowelProportions.append(vowelsCount / len(word))

    meanProportions = sum(vowelProportions) / len(vowelProportions)
    print "Mean proportions: ", meanProportions

    pylab.figure(1)
    pylab.hist(vowelProportions, bins=15)
    pylab.title("Histogram of Proportions of Vowels in Each Word")
    pylab.ylabel("Count of Words in Each Bucket")
    pylab.xlabel("Proportions of Vowels in Each Word")

    ymin, ymax = pylab.ylim()
    ymid = (ymax - ymin) / 2
    pylab.text(0.03, ymid, "Mean = {0}".format(
        str(round(meanProportions, 4))))
    pylab.vlines(0.5, 0, ymax)
    pylab.text(0.51, ymax - 0.01 * ymax, "0.5", verticalalignment = 'top')

    pylab.show()

    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
