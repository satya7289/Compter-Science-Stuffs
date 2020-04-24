# https://www.hackerrank.com/challenges/maxsubarray/problem

def maxSubarray(arr):
    # for subarray
    n = len(arr)
    # temp = []
    # for i in range(n):
    #     x,y = arr[i],arr[i]
    #     for j in range(i+1,n):
    #         y += arr[j]
    #         x = max(y,x)
    #     temp.append(x)
    Global_max = arr[0]
    Curr_max = arr[0]
    for i in range(1,len(arr)):
        Curr_max = max(arr[i], Curr_max+arr[i])
        Global_max = max(Global_max, Curr_max)

    # subsequence sum
    m = max(arr)
    s=0
    for i in arr:
        if i>0:
            s += i
    if s==0:
        ans =m
    else:
        ans = s
    return [Global_max,ans]

print(maxSubarray([-2 ,-3, -1 ,-4 ,-6]))