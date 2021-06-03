import random as rnd

def generateRandomValues(size, lower, upper):
    collection = []
    for x in range(size):
        collection.append(rnd.randint(lower, upper) + .3)
    return collection
