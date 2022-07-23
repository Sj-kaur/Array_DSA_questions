
def fact(n):
    if n == 1:
        return 1
    else:
        factorial = n * fact(n-1)
        return factorial

if __name__ == "__main__":
    n = int(input("Enter the integer to find it's factorial: \n"))
    print("The factorial of ", n , "is: ", fact(n))