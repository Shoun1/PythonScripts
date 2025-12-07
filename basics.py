#functional programming
my_list=(2,5,8,10)

double_mylist = list(map(lambda x:x**2,my_list))
print(double_mylist)

inputs = [0.8, 0.5, 0.2]
weights = [0.6, 0.3, 0.1]
weighted_avg = sum(x*w for x, w in zip(inputs, weights))
print(weighted_avg)

print("Enter some values: ")

arr = list(map(int,input().split(' ')))
print(arr)

#remove duplicates
def remove_duplicates(arr):
    i = 0

    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            arr[i] = arr[j]
            i = i+1

    return i+1

indx = remove_duplicates(arr)
for i in range(indx):
    print(arr[i])
