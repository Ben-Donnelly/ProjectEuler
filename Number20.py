from time import time
from math import factorial
start = time()

x = f"{factorial(100)}"
sum_dig = sum([int(i) for i in x])
print(sum_dig)

print(f"Took {time() - start} seconds")
