# This code will not work for the array which has all negative elements.

def maxSubArraySum(arr,n):
    max_far = arr[0]
    max_end_here = 0

    for i in range(n):
        max_end_here = max_end_here + arr[i]
        if max_end_here < 0:
            max_end_here = 0
        elif max_end_here > max_far:
            max_far = max_end_here
    return max_far

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    print(maxSubArraySum(arr,n))
