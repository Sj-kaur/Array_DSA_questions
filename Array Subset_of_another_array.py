
def check_subset(arr1,arr2,n1,n2):
    i = 0
    j = 0
    for i in range(n2):
        for j in range(n1):
            if arr2[i] == arr1[j]:
                break
        if j == (n1-1):
            return 0
    return 1



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
    
    if (check_subset(arr1,arr2,n1,n2)):
        print("Yes, arr2 is a subset of arr1")
    else:
        print("No, arr2 is not a subset of arr1")