a = 0
for a in range(100):
    if(a % 7 == 0 or a % 10 == 7 or a // 10 == 7):
        continue
    print(a)
    a = a+1

