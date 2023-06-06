def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    # your code goes here
    for x in range(a, b):
        if isPrime(x):
            yield x


f = int(input("Provide lower limit : "))
t = int(input("Provide upper limit : "))

print(list(primeGenerator(f, t)))
