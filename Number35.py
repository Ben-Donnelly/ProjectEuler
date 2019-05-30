#NOPE
def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False

    for k in range(3, int(num ** 0.5) + 1, 2):
        if num % k == 0:
            return False
    return True

l = []
for i in range(100):
    number = str(i)
    for j in range(len(number)):
        rotatedNumber = number[j:len(number)] + number[0:j]
        if is_prime(int(i)) and int(rotatedNumber)== i:
            l.append(rotatedNumber)
            break
print(l)