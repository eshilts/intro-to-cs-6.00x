def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]

def makePositive(num):
    return abs(num)

applyToEach(testList, makePositive)
print testList


testList = [1, -4, 8, -9]

def addone(num):
    return num + 1

applyToEach(testList, addone)
print testList


testList = [1, -4, 8, -9]

def square(num):
    return num * num

applyToEach(testList, square)
print testList
