import numpy as np
arr = np.random.rand(5,5)
array = np.copy(arr)
arr1=[]
for col in range(1,6):
    sub_arr = arr[:5,col-1] #colth column
    max1 = np.max(sub_arr) #largest value in col
    sub_arr[sub_arr == max1] = 0
    max2 = np.max(sub_arr)
    arr1.append(max2)
arr2 = np.array(arr1)
print(array)
print(arr2)

