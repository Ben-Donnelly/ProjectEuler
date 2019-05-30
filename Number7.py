from math import sqrt
from sys import maxsize
from time import time

start = time()


def is_prime(n):

    for j in range(2, int(sqrt(n))+1):
        if n % j == 0:
            return False
    return True


count = 0

for i in range(2, maxsize):
    if is_prime(i):
        count += 1
    if count == 10001:
        print(f"10001st prime: {i}")
        break

print(f"Took {time() - start} seconds")
