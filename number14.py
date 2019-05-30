from time import time
start = time()
greatest = 0
count = 0
terms = ['', '']
for i in range(1000000, 2, -1):
    while i > 2:
        temp = i
        count = 1
        while i != 1:
            if i % 2 == 0:
                i /= 2
                count += 1
            else:
                i = (3*i + 1)
                count += 1
        if count > greatest:
            greatest = count
            terms[0] = temp
            terms[1] = greatest
        i = i - 1

print(f"{terms[0]} produces {terms[1]}")
print(time() - start)
