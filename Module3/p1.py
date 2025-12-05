import numpy as np
arr = np.array(range(17))
#arr1 = np.repeat(arr,2,axis=0)
#arr1 = np.random.rand(5,5)
#arr1 = arr[0:2,0:2]
#arr1 = np.array([[10,11,12],[13,14,15],[16,17,18]])
#cat = np.concatenate((arr,arr1),axis=1)
#arr = np.array(range(8)).reshape(2,2,2)
'''arr1=[]
print("Enter dimensions: ")
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
print("Enter values: ")
for i in range(m):
    r=[]
    for j in range(n):
        r.append(int(input()))
    arr1.append(r)
array = np.array(arr1)'''
#arr2 = np.concatenate((arr,array))
#print(arr2)
#array_split = np.vsplit(arr,2)
#print(arr1)
#split1 = np.split(arr,2)
split2 = np.array_split(arr,4)
#split3 = np.hsplit(arr,2)
#split4 = np.vsplit(array,4)
#print(split1)
print(split2)
#print(split3)
#print(split4)
