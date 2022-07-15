# USING SLICING METHOD
# THIS WILL CYCLICALLY ROTATE THE ARRAY FROM RIGHT SIDE BY ONE.

def rotate_array(arr,n):
    arr_new = []
    arr1 = arr[:n-1]
    arr2 = arr[n-1]
    arr_new.append(arr2)
    for i in range(len(arr1)):
        arr_new.append(arr[i])
    return arr_new

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print("The rotated array is : ", rotate_array(arr,n))















