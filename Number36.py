from time import time
start = time()


def is_pal(x, y):
    if x == x[::-1] and y == y[::-1]:
        return True


sum_x = 0
for i in range(1, 1000000, 2):
    if is_pal(str(i), str(bin(i)[2:])):
        sum_x += i

end = time()

print(sum_x)
print(end - start)
