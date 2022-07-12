# METHOD - 1

def reverse_array(arr,n):
    for i in range(n):
        for j in range(i+1,):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp 
    return arr
            
n = int(input("Enter the length of array: \n"))
print("Enter the elements : ")
arr =[]
for i in range(n):
    value = int(input())
    arr.append(value)
print("The array is : ",arr)
print("The reversed array is: ",reverse_array(arr,n))


# METHOD - 2

def reverse_array(arr):
    return arr[::-1]


n = int(input("Enter the length of array: \n"))
print("Enter the elements : ")
arr =[]
for i in range(n):
    value = int(input())
    arr.append(value)
print("The array is : ",arr)
print("The reversed array is: ",reverse_array(arr))



