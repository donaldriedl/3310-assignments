import sys
import random

def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def isPrimeMiller(n):
    if n == 2:
        return True
    for i in range(20):
        b = random.randrange(2, n)
        ok = miller(n, b)
        if not ok:
            return False
    return True

def miller(n, b):
    if n % b == 0:
        return False
    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1
    x = pow(b, t, n)
    if x == 1 or x == n - 1:
        return True
    for i in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False
    
if __name__ == "__main__":
    if sys.argv[1] == "test":
        for i in range(3, 1000000):
            if isPrime(i) != isPrimeMiller(i):
                print("Failed", i)
                sys.exit(0)
        print("OK")
    else:
        n = int(sys.argv[1])
        if isPrimeMiller(n):
            print("Prime")
        else:
            print("Not Prime")