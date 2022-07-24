def  findMinDiff(arr,n,m):

    if n == 0 or m == 0:
        return 0
    if n < m:
        return -1 

    min_diff = arr[n-1] - arr[0]

    for i in range(n-m+1):
        min_diff = min(min_diff, arr[i+m-1] - arr[i])
    return min_diff
   
if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    m = int(input("Enter the number of students: "))
    arr.sort()
    print("The minimum difference between the maximum number of chocolates and minimum number of chocolates is : ",findMinDiff(arr,n,m))