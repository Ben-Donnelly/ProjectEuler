from time import time
start = time()

sq_sum = sum(i for i in range(101))
sum_sq = sum(i ** 2 for i in range(101))


print(sq_sum ** 2 - sum_sq)
print(f"Took {time() - start} seconds")
