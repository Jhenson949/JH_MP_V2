import random
randomNumbers = []
for outer in range(10):
    randomNumbers.append([])
    for inner in range(10):
        number = random.randint(1, 4)
        randomNumbers[outer].append(number)
print(randomNumbers)
