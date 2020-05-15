# https://www.hackerrank.com/challenges/stockmax/problem

def stockmax(prices):
    profit =0
    cur_max = prices[-1]
    n = len(prices)
    for i in range(0,n-1):
        idx = n-i-2
        if prices[idx]<cur_max:
            profit += cur_max - prices[idx]
        else:
            cur_max = prices[idx]
        # print(profit,idx)
    return profit

print(stockmax([1,5,2,4,0,3,0,1,2]))