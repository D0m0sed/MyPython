A = [1, 2, 3, 4, 5]
'''for x in A:
    #print(x, type(x))
    x += 1
    #print(x)
print(A)
for k in range(4):
    A[k] = A[k]*A[k]
    #print(A[k])'''
c = list(A)
print(c)