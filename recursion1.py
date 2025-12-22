def printans(n):
    if n == 0:
        return
    
    printans(n-1)
    print(n)

printans(5)

