primes = [2]

def isPrime(x):
        for i in range(2, int(x ** .5) + 1):
            if not x % i: 
                return False
        return True
        
n=int(input())
biggest_prime = primes[-1]
if n > biggest_prime:
    for i in range(biggest_prime + 1, n + 1):
        if isPrime(i): 
            primes.append(i)
if sum(i <= n for i in primes) % 2 :
    print("Alice")
else:
    print("Bob")


