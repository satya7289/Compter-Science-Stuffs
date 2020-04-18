

def fibonacciModified(t1, t2, n):
    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = t1, t2
    for i in range(2,n+1):
        dp[i] = dp[i-2] + (dp[i-1] * dp[i-1])
    # return nth value
    return dp[n-1]

print(fibonacciModified(0, 1, 5))