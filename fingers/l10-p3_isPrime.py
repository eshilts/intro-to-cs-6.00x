def isPrime(n):
    if type(n) != type(1):
        raise TypeError
    if n <= 0:
        raise ValueError

    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
            if len(divisors) > 1:
                return False

    return True

print isPrime(1)
print isPrime(2)
print isPrime(4)
print isPrime(11)
print isPrime(29)
print isPrime(100)
