def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    
    lengthSum = 0.0

    for word in L:
        lengthSum += len(word)

    lengthMean = lengthSum / len(L)

    deviationSum = 0.0
    for word in L:
        deviationSum += (float(len(word)) - lengthMean) ** 2

    return (deviationSum / len(L)) ** (1.0/2.0)

print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
