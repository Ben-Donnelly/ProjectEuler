#NOPE
# import time

start = int(round(time.time() * 1000000000))

def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
         computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

def main():
    sum = 0
    i = 0
    while (fib(i) < 4000000):
        if(fib(i) % 2 == 0):
            sum += fib(i)
        i += 1
    print(sum)
main()

end = int(round(time.time() * 1000000000))

print("Took %s nanoseconds" % (end - start))