num = int(input())

revNum = 0

while num > 0:
    ld = num % 10
    revNum = (revNum * 10) + ld
    
    num //= 10

print(revNum)
