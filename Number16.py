from time import time

start = time()
x = f"{2**1000}"

sum_dig = sum([int(i) for i in x])
print(sum_dig)

print(f"Took {time() - start} seconds")
