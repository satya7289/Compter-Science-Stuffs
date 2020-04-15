def foo(n,c):
    c.sort()
    dp = [[ 0 for i in range(len(c))] for j in range(n+1)]

    # filling first colunm
    for i in range(1,n+1):
        if i% c[0]==0:
            dp[i][0] = 1

    # filling table
    for j in range(1,len(c)):
        for i in range(0,n+1):
            if i<c[j]:
                dp[i][j] = dp[i][j-1]
            elif i==c[j]:
                dp[i][j] = dp[i][j-1] +1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-c[j]][j]
           
    # for i in dp:
    #     print(i)
    return dp[n][len(c)-1]

foo(10,[2, 5, 3, 6])