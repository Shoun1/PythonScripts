import numpy as np
'''str1=[]
ind=0
print("Enter no. of text lines: ")
n = int(input())
print("Enter text: ")
for i in range(n):
    text = input()
    item=text.split(' ')
    str1.append(item)
arr = np.array(str1,dtype='object')
#array_split = np.split(arr,n)
print(arr)'''
arr=[]
print("Enter dimensions: ")
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
print("Enter values: ")
for i in range(m):
    r=[]
    for j in range(n):
        r.append(int(input()))
    arr.append(r)
array = np.array(arr)
print("Enter column: ")
col = int(input())
print(array)
print("\n")
array_sorted = np.sort(array[:m,col-1])
array[:m,col-1] = array_sorted
print(array)
        
