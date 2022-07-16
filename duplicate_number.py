# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

def repeated_number(arr,n):
    arr.sort()
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            return arr[i]


if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    n = n+1
    print("Enter the elements of the array and also repeat any one element: ")
    arr =[]
    for i in range(1,n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print("The repeated number in the array is: ",repeated_number(arr,n))