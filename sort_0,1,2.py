# METHOD - 1

n = int(input("Enter the length of array: \n"))
print("Enter the elements 0 ,1 and 2 only for the array : ")
arr =[]
for i in range(n):
    value = int(input())
    if (value == 0) or (value == 1) or (value == 2):
        arr.append(value)
    else:
        print("you have entered the wrong value , enter 0,1 or 2 only.")
print("The array is : ",arr)
arr.sort()
print(arr)

# METHOD - 2

def sort_0_1and2(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                pass
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            if arr[i] < arr[j]:
                pass
    return arr


if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements 0 ,1 and 2 only for the array : ")
    arr =[]
    for i in range(n):
        value = int(input())
        if (value == 0) or (value == 1) or (value == 2):
            arr.append(value)
        else:
            print("you have entered the wrong value , enter 0,1 or 2 only.")
    print("The array is : ",arr)
    print("The sorted array is: ",sort_0_1and2(arr,n))
