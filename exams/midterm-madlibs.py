##### generateForm

def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    madlibStoryWords = []
    storyWords = story.split(' ')

    for word in storyWords:
        if word in listOfAdjs:
            madlibStoryWords.append("[ADJ]")
        elif word in listOfNouns:
            madlibStoryWords.append("[NOUN]")
        elif word in listOfVerbs:
            madlibStoryWords.append("[VERB]")
        else:
            madlibStoryWords.append(word)

    return ' '.join(madlibStoryWords)

##### generateTemplates

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    madlibsTemplate = []

    for word in madLibsForm.split(' '):
        if word in ['[ADJ]', '[VERB]', '[NOUN]']:
            madlibsTemplate.append(word)

    return madlibsTemplate


#### verifyWord

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[VERB]':
        return userWord in listOfVerbs
    else:
        return userWord in listOfNouns



# Test cases
 # Story 1
story = 'The ravenous zombies started attacking yesterday'
print "Testing story: ", story
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']

actual = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
expected =  "The [ADJ] [NOUN] started [VERB] [NOUN]"
print actual
print expected
assert actual == expected

template = generateTemplates(actual)
print template

assert verifyWord('ravenous', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('humans', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('zombies', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('attacking', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('attacks', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('flies', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('balloon', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('succulent', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)

 # Story 2
story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
print "Testing story: ", story
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

actual = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
expected = "At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear"
print actual
print expected
assert actual == expected

template = generateTemplates(actual)
print template

assert verifyWord('creepy', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('plaid', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('store', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('grandpa', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('found', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('looked', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('flies', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('balloon', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
print "Should be false: ", verifyWord('succulent', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
