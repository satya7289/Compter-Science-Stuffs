# https://www.hackerrank.com/challenges/abbr/problem

def abbreviation(a, b):
    n, m = len(a), len(b)
    dp = [[ 0 for i in range(m+1)] for j in range(n+1)]

    # filling 1st row
    dp[0][0] =1

    # filling 1st colunm
    for i in range(1,n+1):
        if a[i-1].islower():
            dp[i][0] = 1
        else:
            dp[i][0] = 0
        
    # filling table

    for i in range(1,n+1):
        for j in range(1,m+1):
            i_index = i-1
            j_index = j-1
            if a[i_index].isupper():
                if b[j_index]==a[i_index].upper() and dp[i-1][j-1]!=0:
                    dp[i][j]=1
                else:
                    dp[i][j]=0
            
            if a[i_index].islower():
                if dp[i-1][j]!=0:
                    dp[i][j] = dp[i-1][j]
                else:
                    if b[j_index] == a[i_index].upper() and dp[i][j-1]!=0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=0
            
    for i in dp:
        print(i)
    if dp[n][m]==1:
        return "YES"
    else:
        return "NO"

print(abbreviation("AbcDE","ABDE"))


# TODO: test case fail
# ANS: NO, GIVES: YES
# abcdefghijklmnopqrstuvwxyzababababAbAbaBabAbababababAbababaBabaBabAbaBababababababababaBababaBababababaBabaBabababABabababAbabababaBAbababababababababababAbababaBabababAbabababababababaBaBabAbabaBababababababababaBAbabaBAbabAbababababaBababAbababababababaBabababababaBaBaBababababAbabaBababaBaBabababababababababababababababababababAbababababababababAbababaBababababababababAbabaBabababaBAbabababababababababababababababaBababAbabababaBAbababababaBabababababababaBaBabababababababAbababababababababAbabababaBabAbabaBabAbAbabAbaBabababababaBaBababABabababababAbaBababababababaBabababababababababababAbababababababababababababababababaBabababababababababababababababAbabaBababababababababababaBAbabababAbababababababababaBabababaBaBabababababababababaBababAbaBababAbababababaBAbababaBababababababAbABabababAbababaBababababababaBaBababababAbAbabababababababababaBababababababababababababababababaBabababAbabAbababababABabababAbabababababababababaBabABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBABCDEFGHIJKLMNOPQRSTUVWXYZ
