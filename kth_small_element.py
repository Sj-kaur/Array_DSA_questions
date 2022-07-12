def kth_smallest_element(arr,n,k):
    if n > k:
        return arr[k]
    else:
        return "The kth value entered is greater than the number of elements."

n = int(input("Enter the length of array: \n"))
k = int(input("Enter the smallest element number to find. It should be less than the number of elements. "))
print("Enter the elements : ")
arr =[]
for i in range(n):
    value = int(input())
    arr.append(value)
print("The array is : ",arr)
arr.sort()
print("Sorted array is :",arr)
print("The kth smallest element is : ",kth_smallest_element(arr,n,k))