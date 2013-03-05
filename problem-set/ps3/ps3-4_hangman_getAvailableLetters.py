def getAvailableLetters(lettersGuessed):
  '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
  available = ''

  for letter in string.ascii_lowercase:
    if letter not in lettersGuessed:
      available += letter

  return available
