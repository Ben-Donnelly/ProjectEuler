#NOPE

import math
n = 7
o = (1+math.sqrt(5))/2
y = (1-math.sqrt(5))/2

for i in range(2, 1000000**1000000):
    nth = round((o ** i - y ** i) / math.sqrt(5))
    if len(str(nth)) > 10:
        print(nth)
        quit()
# import time
#
# start = time.time()
#
#
# fib = [0, 1]
#
# i = 2
#
# while True:
#     fib_new = fib[i-1]+fib[i-2]
#     fib.append(fib_new)
#     if fib_new > 10**999:
#         print(i)
#         break
#     i = i+1
#
# end = time.time()
#
# print(end-start)
#
#
#
#
#
#
# import sys
#
# def main():
#     terms = 0
#     for i in range(1, sys.maxsize):
#         x = fib(n-1)+fib(n-2)
#
#         while(x > 0):
#             terms += 1
#             x //= 10
#         if terms > 999:
#             print(fib(i), terms)
#             break
#
# main()
#
# # a = 1
# # b = 1
# # result = 2
# # while len (str(b)) < 1000:
# #     a, b = b, a + b
# #
# #     result += 1
# # print (result)