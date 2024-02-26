"""
Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?

largestPrimeFactor(2) should return a number.
largestPrimeFactor(2) should return 2.
largestPrimeFactor(3) should return 3.
largestPrimeFactor(5) should return 5.
largestPrimeFactor(7) should return 7.
largestPrimeFactor(8) should return 2.
largestPrimeFactor(13195) should return 29.
largestPrimeFactor(600851475143) should return 6857.
"""

def largestPrimeFactor(n):
    """
    Starting with 2, we want to divide n by every number we can up until we reduce n to it's largest prime.
    ie: 168 /2 -> 84 /2 -> 42 /2 -> 21 /2 nope /3 -> 7 and 7 is found to be prime
    Notice, after 2, we can skip each factor check by 2 and iterate over odds only
    """
    prime = 1
    k = range(1, n, 2)

    for i in k:
        if i == 1:
            continue

        while n%i == 0:
            if i>prime:
                prime = i
                
            n = int(n/i)
        
        if n == 1:
            break

    return prime

if __name__ == "__main__":
    n = 600851475143
    print(largestPrimeFactor(n))