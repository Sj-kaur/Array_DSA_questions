def kth_smallest_element(arr,n,k):
    if n > k:
        return arr[k-1]

if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    k = int(input("Enter the smallest element number to find. It should be less than the number of elements. "))
    print("Enter the elements : ")
    arr =[]
    for i in range(1,n+1):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    arr.sort()
    print("Sorted array is :",arr)
    print(k ,"th smallest element is : ",kth_smallest_element(arr,n,k))


       
