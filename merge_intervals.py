def merge(arr):
    arr.sort()
    stack = []
    stack.append(arr[0])
    for i in arr[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1],i[-1])
        else:
            stack.append(i)

    return stack

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
    print(merge(intervals))