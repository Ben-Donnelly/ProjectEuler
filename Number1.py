from time import time
start = time()

sum_x = 0
for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_x += i
print(sum_x)


print("Took %s seconds" % (time() - start))
