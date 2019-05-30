from sys import maxsize
from time import time

start = time()

for i in range(2520, maxsize, 2520):
    if all([i % x == 0 for x in range(2, 21)]):
        num = i
        print(num)
        break

print(f"Took {time() - start} seconds")
