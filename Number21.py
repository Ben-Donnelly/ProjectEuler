from time import time
start = time()


def even_div(num):
    am_sum = 0
    for j in range(1, int(num/2)+1):
        if num % j == 0:
            am_sum += j
    return am_sum


y = 0
for i in range(1, 10000):
    x = even_div(i)

    if even_div(x) == i and x != i:
        y += i
print(f"{y}\nTook {time()-start} seconds")
