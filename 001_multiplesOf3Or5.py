"""
Problem 1: Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

multiplesOf3Or5(10) should return a number.
multiplesOf3Or5(49) should return 543.
multiplesOf3Or5(1000) should return 233168.
multiplesOf3Or5(8456) should return 16687353.
multiplesOf3Or5(19564) should return 89301183.
"""

def multiplesOf3Or5(number):
    multiples = []
    for i in range(number):
        if i%3 == 0:
            multiples.append(i)
        elif i%5 ==0:
            multiples.append(i)
    
    return sum(multiples)

if __name__ == "__main__":
    number = 1000
    print(multiplesOf3Or5(number))