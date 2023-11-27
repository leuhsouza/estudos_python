def minSum(A):
    min_val = min(A)

    return min_val * (len(A)-1)

A = [2, 4, 1, 3]  
print (minSum(A))  