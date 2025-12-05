import numpy as np
'''arr = np.array(range(9)).reshape(3,3)
#b = arr > 2
print(arr[arr>2])'''
import numpy as np
'''arr = np.array([0],dtype=float)
arr1 = np.repeat(arr,10)
arr1[5] = 11
print(arr1)'''
arr1=np.array(['Hello','PHP','JS','examples','html'])
arr2=np.array(['Hello','php','Java','examples','html'])
arr3=[]
for i in range(5):
    common = arr1[i] == arr2[i] #boolean
    arr3.append(common)
array_common = np.array(arr3)
print(arr3)
'''arr = np.array(range(16)).reshape(4,4) 
arr1 = np.repeat(10,4)
arr2 = arr+arr1
print(arr2)
arr1 = np.array([10,20,30])
arr2 = np.array([20,50,60])
#arr = np.array(range(10))
arr3 = np.intersect1d(arr1,arr2)
print(arr3)'''

