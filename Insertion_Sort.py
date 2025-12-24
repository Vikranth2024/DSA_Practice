arr = [6,8,2,4,1]

n = len(arr)

for i in range(1,n):

    k = arr[i]
    j = i-1

    while j >= 0 and arr[j] > k:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = k
    
print(arr)
