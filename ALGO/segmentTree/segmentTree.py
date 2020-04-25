from math import ceil, log2

def STutil(arr,st,low,high,pos):

    if low==high:
        st[pos] = [1,arr[low]]
        return
    
    mid = (low+high)//2
    STutil(arr,st,low,mid,2*pos+1)
    STutil(arr,st,mid+1,high,2*pos+2)

    left = st[2*pos+1]
    right = st[2*pos+2]

    if left[1]==right[1]:
        st[pos] = [left[0]+right[0], left[1]]
    elif left[1]>right[1]:
        st[pos] = left
    else:
        st[pos] = right
    

def ST(s):
    x = ceil(log2(len(s)))
    max_size = 2*(2**x) -1
    st = [[0,'']]*max_size

    STutil(s,st,0,len(s)-1,0)
    return st


def queryST(st,qlow,qhigh,low,high,pos):
    if qlow<=low and qhigh>=high:
        return st[pos]
    if qlow > high or qhigh<low:
        return [0,'']

    mid = (low+high)//2
    left = queryST(st,qlow,qhigh,low,mid,2*pos+1)
    right = queryST(st,qlow,qhigh,mid+1,high,2*pos+2)
    if left[1]>right[1]:
        return left
    elif left[1]<right[1]:
        return right
    else:
        return [left[0]+right[0],right[1]]



def getMaxCharCount(s, queries):
    t = ''
    for i in s:
        if i.islower():
            t += i.upper()
        else:
            t+= i
    st = ST(t)
    # print(st)
    ans =[]
    for q in queries:
        ans.append(queryST(st,q[0],q[1],0,len(t)-1,0)[0])
        
    return ans
