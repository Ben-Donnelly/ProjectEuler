from time import time
s = time()
x, y, z = 1, 1, 0

result = 0

while z < 4000000:
    z = x + y
    if z % 2 == 0:
       result += z
    x, y = y, z

print(f"{result}\nTook: {time() - s} seconds")

# 4613732
# Took: 0.0 seconds
