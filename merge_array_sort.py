# Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.

def merge_without_space(arr1,arr2):
    arr = arr1 + arr2
    arr.sort()
    return arr

if __name__ == "__main__":
    n1 = int(input("Enter the length for first array: \n"))
    print("Enter the elements : ")
    arr1 = []
    for i in range(n1):
        value = int(input())
        arr1.append(value)

    n2 = int(input("Enter the length for second array: \n"))
    print("Enter the elements : ")
    arr2 = []
    for i in range(n2):
        value = int(input())
        arr2.append(value)

    arr1.sort()
    arr2.sort()
    print("Merged array without any extra space : ",merge_without_space(arr1,arr2))