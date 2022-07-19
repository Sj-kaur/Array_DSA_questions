def union_of_array(arr1,arr2):
    arr = arr1 + arr2
    return set(arr)

def intersection_of_array(arr1,arr2,n1,n2):
    arr = []
    if n1 == n2 :
        for i in range(n1):
            for j in range(n2):
                if arr1[i] == arr2[j]:
                    arr.append(arr1[i])
    elif n1 > n2:
         for i in range(n1):
                for j in range(n2):
                    if arr1[i] == arr2[j]:
                        arr.append(arr1[i])
    elif n1 < n2:
         for i in range(n2):
                for j in range(n1):
                    if arr2[i] == arr1[j]:
                        arr.append(arr2[j])
    return set(arr)


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
    print("The first sorted array is : ",arr1)
    print("The second sorted array is : ",arr2)
    print("The union of array1 and array2 is :", union_of_array(arr1,arr2))
    print("The intersection of array1 and array2 is :", intersection_of_array(arr1,arr2,n1,n2))
