

def maxProfit(price):
    max_profit = 0
    for i in range(len(price)-1):
        for j in range(i+1,len(price)):
            profit = price[j] - price[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit   

            



if __name__ == "_main__":
    n = int(input("Enter the length of array containing prices of stock: \n"))
    print("Enter the prices : ")
    price =[]
    for i in range(1,n+1):
        value = int(input())
        price.append(value)
    print("The prices of stocks is : ",price)
    print("The max profit is: " ,maxProfit(price)) 


       