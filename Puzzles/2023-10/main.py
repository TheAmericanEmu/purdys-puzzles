from itertools import count


count=1
sum = 0
while count != 10000000:
    num = list(str(count))
    cub_sum = 0
    for n in num:
        n = int(n)
        cub_sum+= n**3
    if cub_sum == 789:
        sum+= count
    count+=1
print(sum)
