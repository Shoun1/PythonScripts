import numpy as  np
arr = np.array(range(16)).reshape(4,4)
print(arr[np.ix_([2,0,3],[1,2,0])])
#print(arr[[-1,0,1]])
#print(arr[[1,0,-1]])
'''nparr = np.linspace(1,3,endpoint=False)
revarr = np.array(nparr[-1:-7:-1])
print(revarr)
def accept(r,c):
    arr=[]
    for i in range(r):
        r=[]
        for j in range(c):
            val = int(input())
            r.append(val)
        arr.append(r)
    mat = np.array(arr)
    return mat
def display(mat3,x,p):
    for i in range(x):
        for j in range(p):
            print(mat3[i][j],end=" ")
    print("\n")
print("Enter N,M,P:")
n,m,p = int(input()),int(input()),int(input())
mat1 = accept(n,p)
mat2 = accept(m,p)
mat3 = np.concatenate((mat1,mat2),axis=0).reshape(n+m,p)
x = n+m
display(mat3,x,p)'''
