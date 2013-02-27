def isIn(char, aStr):
  '''
  char: a single character
  aStr: an alphabetized string

  returns: True if char is in aStr; False otherwise
  '''

  length = len(aStr)
  check = int(length / 2)

  if length == 0:
    return False

  if length == 1:
    if aStr == char:
        return True
      else:
        return False

  if aStr[check] == char:
    return True
  elif char < aStr[check]:
    return isIn(char, aStr[0:check])
  else:
    return isIn(char, aStr[check + 1:length])

