#NOPE
# import sys
import time
x = []

for i in range(1, sys.maxsize):
    x.append(j for j in range(1, i) if j % i == 0)
    print(x)
    if len(x) > 5:
        print(sum(x), x)
        break
# print(sum(x))


number = [sum(x) for x in range(10)]
print(number)





# Not done





'''
s1 = 0
count = 0


def factors(n):
    return set(x for tup in ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)


def main():
    for i in range(1, sys.maxsize**10):
        res = sum(x for x in range(1, i + 1))

        if factors(res).__len__() > 500:
            print(res)
            break


start = time.time()
main()
elapsed = (time.time() - start)

print("found in %s seconds" % elapsed)

'''


# s1 = 3434
# 3434989