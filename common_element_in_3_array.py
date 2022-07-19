# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.


from collections import Counter

def intersection_of_array(arr1,arr2,arr3):
    '''First convert all three lists into dictionaries having elements as keys and their frequencies as value, using Counter() method'''
    arr1 = Counter(arr1)
    arr2 = Counter(arr2)
    arr3 = Counter(arr3)

    # perform intersection operation
    result = dict(arr1.items() & arr2.items() & arr3.items())
    common = []

    for (key , val) in result.items():
        for i in range(0,val):
            common.append(key)
    return common
    

if __name__ == "__main__":
    n1 = int(input("Enter the length for first array: \n"))
    print("Enter the elements : ")
    arr1 = []
    for i in range(n1):
        value = int(input())
        arr1.append(value)

    n2 = int(input("Enter the length for second array: \n"))
    print("Enter the elements : ")
    arr2 = []
    for i in range(n2):
        value = int(input())
        arr2.append(value)

    n3 = int(input("Enter the length for third array: \n"))
    print("Enter the elements : ")
    arr3 = []
    for i in range(n3):
        value = int(input())
        arr3.append(value)
        
    arr1.sort()
    arr2.sort()
    arr3.sort()
    print("The intersection of array1 and array2 is :", intersection_of_array(arr1,arr2,arr3))