import numpy as np
def test(arr1,arr2,ch):
    arr3=[]
    for i in range(5):
        if ch == '==':
            obj = arr1[i] == arr2[i]
        elif ch == '>=':
            obj = arr1[i] >= arr2[i]
        elif ch == '<=':
            obj = arr1[i] <= arr2[i]
        elif ch == '>':
            obj = arr1[i] > arr2[i]
        else:           #if ch == '<':
            obj = arr1[i] < arr2[i]
        arr3.append(obj)
    arr = np.array(arr3)
    return arr
arr1 = np.array(['Hello','PHP','JS','examples','html'])
arr2 = np.array(['Hello','php','Java','examples','html'])
array_test1 = test(arr1,arr2,'==')
array_test2 = test(arr1,arr2,'>=')
array_test3 = test(arr1,arr2,'<=')
array_test4 = test(arr1,arr2,'>')
array_test5 = test(arr1,arr2,'<')
print(array_test1)
print(array_test2)
print(array_test3)
print(array_test4)
print(array_test5)
