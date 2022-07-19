# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
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