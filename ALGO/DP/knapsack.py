# https://www.hackerrank.com/challenges/unbounded-knapsack/problem

def unboundedKnapsack(k, arr):
    arr.sort()

    dp = [[0 for i in range(k+1)] for j in range(len(arr)+1)]

    # filling table
    for i in range(1,len(arr)+1):
        i_index = i-1
        for j in range(arr[i_index],k+1):
            if dp[i-1][j] == j:
                dp[i][j] = j
            else:
                if j%arr[i_index]==0:
                    dp[i][j]=j
                else:
                    temp = max(dp[i-1][j],dp[i][j-1])
                    l = 1
                    while 1:
                        j_index = j-arr[i_index]*l
                        if j_index >= 0:
                            temp = max(dp[i-1][j_index]+(arr[i_index]*l),temp)
                            l += 1
                        else:
                            break
                    dp[i][j] = temp
                    

            if dp[i][j]==k:
                return k

    return dp[len(arr)][k]

unboundedKnapsack(10,[2,3,4])

