import random as rnd
rnd.seed(1024)
randomInts = [rnd.randint(1, 100) for _ in range(1, 100)]

numEvens = len(list(filter(lambda x: x % 2 == 0, randomInts)))
numOdds = len(list(filter(lambda x: x % 2 != 0, randomInts)))

print(f"Number of evens: {numEvens}.  Number of odds: {numOdds}")


