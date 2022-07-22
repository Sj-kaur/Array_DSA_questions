
def count_pair(arr,k,n):
    count_of_pair = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j] == k:
                count_of_pair += 1
    return count_of_pair


if __name__ == "__main__":
    n = int(input("Enter the length of array: \n"))
    print("Enter the elements : ")
    arr =[]
    for i in range(n):
        value = int(input())
        arr.append(value)
    print("The array is : ",arr)
    k = int(input("Enter any integer: "))
    print("The number of pairs of elements in the array whose sum is equal to ",k , "is: ",count_pair(arr,k,n) )