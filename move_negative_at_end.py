# METHOD -1 
# IN THIS METHOD FIRST WE WILL MAKE TWO LIST OF ARRAY ONE WILL BE "arr1" WHICH WILL CONTAIN ALL THE POSITIVE ELEMENTS OF THE "arr", AND THE SECOND ARRAY WHICH IS "arr2"WILL CONTAIN THE NEGATIVE ELEMENTS OF THE ARRAY. 
# AFTER SEPARATING THE NEGATIVE(arr2) AND POSITIVE(arr1) ELEMENTS OF THE ARRAY(arr) WE WILL CONCATENATE arr1 AND arr2 TO OBTAIN THE OUTPUT.


def mov_negative_at_end(arr,n):
    arr1 = []        #contains positive elements
    arr2 = []        #contains negative elements
    for i in range(n):
        if arr[i] >= 0:
            arr1.append(arr[i])
        if arr[i] < 0:
            arr2.append(arr[i])
    return arr1 + arr2

if __name__ == "__main__":    
    n = int(input("Enter the length of array: \n"))
    print("Enter the positive and negative elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print("The sorted array is : ",mov_negative_at_end(arr,n))


# METHOD - 2
# IN THIS METHOD FIRST WE WILL SORT THE ARRAY AND THEN WE WILL REVERSE IT TO OBTAIN THE DESIRED OUTPUT.

def reverse_array(arr,n):
    for i in range(n):
        for j in range(i+1,):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp 
    return arr

if __name__ == "__main__":    
    n = int(input("Enter the length of array: \n"))
    print("Enter the positive and negative elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    arr.sort()
    print("The sorted array is : ",reverse_array(arr,n))
