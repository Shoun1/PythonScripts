import numpy as np
def accept(m,n,p):
    arr1=[]
    arr2=[]
    print("Enter values for matrix1: ")
    for i in range(m):
        r=[]
        for j in range(n):
            r.append(int(input()))
        arr1.append(r)
    mat1 = np.array(arr1)
    print("Enter values for matrix2: ")
    for i in range(n):
        r=[]
        for j in range(p):
            r.append(int(input()))
        arr2.append(r)
    mat2 = np.array(arr2)
    return mat1,mat2
def compute(mat1,mat2):
    mat3 = np.kron(mat1,mat2)
    return mat3
def display(mat1,mat2,mat4):
    print("MATRIX1\n")
    print(mat1)
    print("MATRIX2\n")
    print(mat2)
    print("KRONECKER PRODUCT MATRIX\n")
    print(mat4)
m = int(input("Enter rows of matrix1: "))
n = int(input("Enter columns of matrix1: "))
p = int(input("Enter columns of matrix2: "))
mat1,mat2=accept(m,n,p)
mat4 = compute(mat1,mat2)
mat4 = mat4.reshape((m*n,n*p))
display(mat1,mat2,mat4)
