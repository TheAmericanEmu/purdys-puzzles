


count=1
sum = 0
digets = []
while count !=10000000:
    if count != 0:
        num = list(str(count))
        cub_sum = 0
        for n in num:
            n = int(n)
            if n != 0:
                cub_sum+= n**3
        if cub_sum == 789:
           for n in num:
                if int(n)!=0:
                    digets.append(n) 
        count+=1

product = 1
for num in digets:
    num=int(num)
    product*=num
print(product%1031)
