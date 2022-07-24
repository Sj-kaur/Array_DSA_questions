# METHOD -2 

def median_array(arr):
    if len(arr)%2 == 0 :
        return ((arr[(len(arr)-1)//2])+arr[(len(arr)-1)//2+1])/2
    else :
        return arr[len(arr)//2]


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
    arr = (arr1 + arr2)
    arr.sort()
    print("The median of two sorted array is :",median_array(arr))


