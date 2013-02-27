def semordnilapWrapper(str1, str2):
  len1, len2 = len(str1), len(str2)
  
  if len1 != len2 or len1 == 1 or len2 == 1 or str1 == str2:
    return False

  def semordnilap(str1, str2):
    len1, len2 = len(str1), len(str2)

    if len1 != len2:
      return False
    
    if len1 == 1:
      if str1 == str2:
        return True
      else:
        return False
    elif str1[0] == str2[-1]:
      return True and semordnilap(str1[1:], str2[:-1])
    

