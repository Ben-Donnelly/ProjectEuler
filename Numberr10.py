from time import time
start = time()


def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False

    for k in range(3, int(num ** 0.5) + 1, 2):
        if num % k == 0:
            return False
    return True


x = sum([i for i in range(1, 2000000, 2) if is_prime(i)]) + 2

print(x)
print(f"Took {time() - start} seconds")
