def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    for i in range(int(n / 24) + 1):
        for j in range(int(n / 8) + 1):
            for k in range(int(n / 5) + 1):
                if 24 * i + 8 * j + 5 * k == n:
                    return True

    return False

def testNumPens(x, expected):
    actual = numPens(x)
    print "PASSES [{3}]: # pens = {0}, expected = {1}, actual = {2}".format(x, expected,
            actual, actual == expected)

testNumPens(0, True)
testNumPens(5, True)
testNumPens(8, True)
testNumPens(13, True)
testNumPens(24, True)
testNumPens(32, True)
testNumPens(48, True)
testNumPens(10*5 + 3*8 + 2*24, True)
testNumPens(1, False)
testNumPens(2, False)
testNumPens(3, False)
testNumPens(4, False)
testNumPens(14, False)
