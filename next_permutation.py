
# Given an array of integers arr, find the next permutation of arr.


def next_permutation(arr):
    i = j = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        return arr.reverse()
    k=i-1
    while arr[j] <= arr[k]:
        j -= 1
    arr[k] , arr[j] = arr[j] ,arr[k]
    l ,r = k + 1 , len(arr) -1
    while l < r:
        arr[l] , arr[r] = arr[r] ,arr[l]
        l += 1
        r -= 1
    return arr





if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr=[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print("The next permutation is :" , next_permutation(arr))
