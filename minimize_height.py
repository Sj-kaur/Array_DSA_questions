# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K.
# Decrease the height of the tower by K ( you can do this operation only if the height of the tower is greater than or equal to K)
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.


def mod_arr(arr,n,k):
    for i in range(0,n):
        if (arr[i] < k):
            arr[i] = arr[i] + k
        elif (arr[i] == k): 
            arr[i] = arr[i] + k
        elif arr[i] > k:
            arr[i] = arr[i] - k
    return arr
    

def get_diff(a,b):
    return a - b

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the height of towers : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    k = int(input("Enter any integer value: "))
    arr = mod_arr(arr,n,k) #modified array
    print("The array can be modified as: ",arr)
    diff = get_diff(max(arr),min(arr))
    print("The difference between the largest and the smallest is: ",diff)
