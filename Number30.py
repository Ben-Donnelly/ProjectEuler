from time import time
start = time()

overall_sum = 0

for i in range(1000, 999999):
    sum_x = 0
    num = i

    while i > 0:
        sum_x += (i % 10) ** 5
        i //= 10

    if sum_x == num:
        overall_sum += sum_x

print(overall_sum)
print(f"Took {time() - start} seconds")
