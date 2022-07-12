# METHOD - 1

def max_min_element(arr):
    a = int(max(arr))
    b = int(min(arr))
    return a ,b 

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print("The maximum and minimum element is :",max_min_element(arr))


# METHOD - 2

def max_min_element(arr,n,arr_max,arr_min):

    if n == 1:
        print("The maximum and minimum element is: ",arr[0], "only.")
    else:
        for i in range(1,n):
            if arr[i] > arr_max:
                arr_max = arr[i]
            if arr[i] < arr_min:
                arr_min = arr[i]
        print("The maximum element is: ",arr_max)
        print("The minimum element is: ",arr_min)

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    arr_max = arr[0]
    arr_min = arr[0]
    max_min_element(arr,n,arr_max,arr_min)





    
