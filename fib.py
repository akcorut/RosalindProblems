def fibb(n, k):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    else:
        return fibb(n-1, k) + k*fibb(n-2, k)

print(fibb(34, 2))