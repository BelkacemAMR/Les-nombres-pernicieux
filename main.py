def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def countPerniciousNumbers(x, y):
    count = 0
    for num in range(x, y+1):
        factors = 0
        for i in range(2, num):
            if num % i == 0 and isPrime(i):
                factors += 1
        if isPrime(factors):
            count += 1
    return count