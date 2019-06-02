from decimal import getcontext, Decimal

getcontext().prec = 102  # Up precision to avoid rounding problems

total = 0
for i in range(100):
    sum_x = str(Decimal(i).sqrt())[:101].replace('.', '')  # Removes decimal
    if len(sum_x) == 1:  # problem states "all the irrational square roots." therefore, remove non-irrational
        continue
    else:
        total += sum(int(j) for j in sum_x)
print(f"Total of digital sum: {total}")
