# Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.


def min_jumps(arr,n):
    jumps = 0
    curr_jump_end = 0
    farthest = 0
    for i in range(n):
        farthest = max(farthest, i + arr[i])
        if i == curr_jump_end:
            jumps += 1
            curr_jump_end = farthest
    return jumps
                       
        
if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr, " here each element represents the max number of steps that can be made forward from that element. ")
    print("The minimum number of jumps is: ", min_jumps(arr,n))
