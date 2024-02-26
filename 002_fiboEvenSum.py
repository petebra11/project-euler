"""
Problem 2: Even Fibonacci Numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.

fiboEvenSum(10) should return a number.
Your function should return an even value.
Your function should sum the even-valued Fibonacci numbers: fiboEvenSum(8) should return 10.
fiboEvenSum(10) should return 10.
fiboEvenSum(34) should return 44.
fiboEvenSum(60) should return 44.
fiboEvenSum(1000) should return 798.
fiboEvenSum(100000) should return 60696.
fiboEvenSum(4000000) should return 4613732.
"""

def fiboEvenSum(n):
    evens = []
    first = 1
    second = 2

    while first <= n:
        # print(f'{first}') # Debug
        if first%2 == 0:
            evens.append(first)

        third = first + second
        first = second
        second = third

    return sum(evens)

if __name__ == "__main__":
    n = 4000000
    print(fiboEvenSum(n))