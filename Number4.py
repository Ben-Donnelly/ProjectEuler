from time import time
start = time()

num = 9009

for i in range(100, 1000):
    for j in range(i, 1000):
        x = str(i*j)
        if x == x[::-1]:
            if (i*j) > num:
                num = i * j
            break
print(num)

print(f"Took {time() - start} seconds ")
