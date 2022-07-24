
def threeWayPartition(arr,a,b,n):
    start = 0
    end = n-1
    i = 0
    while i <= end:
        if arr[i] <= a:
            arr[i] , arr[start] = arr[start] , arr[i]
            i += 1
            start += 1
            
        elif arr[i] > b:
            arr[i] ,  arr[end] = arr[end] , arr[i]
            end -= 1

        else:
            i += 1
    return arr        



if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    a,b = input("Enter the list of range from and to: ").split(",")
    a = int(a)
    b = int(b)
    # list(a,b)
    print("Modified array is :", threeWayPartition(arr,a,b,n))