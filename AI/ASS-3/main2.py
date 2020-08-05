#########################
#
# AI Assignment: 03
# Satya Prakash Sharma
# Date: 05-08-2020
#
#########################


''' USER_OPERATOR TO KEEP TRACK OF OPERATORS'''
USER_OPERATOR = ['|', '&', '!', '>', '=', '(', ')']


''' 
Starts Utilities function for removing Double Implication
And Single Implication
'''
# Method for removing elimation for given two input A and B
def el(A,B):
    if len(A)==1 and len(B)==1:
        return '(' + '!' + A + '|' + B + ')'
    # print('(' + '!' + '(' +A+ ')'+ '|' +  B + ')',"-___________")
    return '(' + '!' + '(' +A+ ')'+ '|' +  B + ')'

# Method for removing double elimation for given two input A and B
def bc(A,B):
    return '(' + '(' + A + '>' + B + ')' + '&' + '(' + B + '>' + A + ')' + ')'

# Method for checking double elimation for given query
def isBC(query):
    for i in query:
        if i=="=":
            return True
    return False

# Method for checking elimation for given query
def isIm(query):
    for i in query:
        if i==">":
            return True
    return False

# Method for converting query to list
def queryToList(query):
    flag =''
    q =[]
    for i in query:
        if i!='!':
            if flag=="":
                q.append(i)
            else:
                if i not in USER_OPERATOR:
                    q.append(flag+i)
                else:
                    q.append(flag)
                    q.append(i)
                flag=''
        else:
            flag += i
    return q

# Method for removing double elimation for given query
def removeBiConditional(query):
    index = 0
    if isBC(query):
        while index<len(query):
            if query[index]=='=':
                temp = bc(query[index-1],query[index+1])
                del query[index-1:index+1+1]
                query.insert(index-1,temp)
                continue

            index += 1
        return ''.join(query)
    else:
        return '(' + ''.join(query) + ')'

# Method for removing elimation for given query
def removeImplication(query):
    index = 0
    if isIm(query):
        while index<len(query):
            if query[index]=='>':
                temp = el(query[index-1],query[index+1])
                del query[index-1:index+1+1]
                query.insert(index-1,temp)
                continue
            index += 1
        return ''.join(query)
    else:
        return '(' + ''.join(query) + ')'

# Utility method for removeDoubleAndSingleImplication
def removeDoubleAndSingleImplicationUtils(query, flag):
    stack =[]
    # print(query)
    for i in range(len(query)):
        # print(stack,i)
        if query[i] !=')':
            if query[i]=='!':
                pass
            else:
                stack.append(query[i])
        else:
            temp_query =[]
            while stack:
                s = stack.pop()
                    
                if s=='(':
                    break
                temp_query.append(s)
            if flag==0:
                y = removeBiConditional(temp_query[::-1])
                # print(y,"________")
                stack.append(y)
            elif flag==1:
                x = removeImplication(temp_query[::-1])
                # print(x,"________",stack)
                stack.append(x)
    # print(stack,"_______")
    if flag==0:
        y = removeBiConditional(stack)
        return y
    if flag==1:
        x = removeImplication(stack)
        return x

# Method for removing double and single implication
def removeDoubleAndSingleImplication(q):    
    if(isBC(queryToList(q))):
        eBI = removeDoubleAndSingleImplicationUtils(queryToList(q),0)
    else:
        eBI = queryToList(q)
    if isIm(eBI):
        eI = removeDoubleAndSingleImplicationUtils(queryToList(eBI),1)
    else:
        eI = eBI
    
    return ''.join(eI)


''' 
End Utilities function for removing Double Implication
And Single Implication.
'''

''' 
Starts Utilities function for Generating Truth Table 
and Evalute Expression. Convert it to CNF.
'''


# Method for finding number of variables in the query: Return set of variables
def findDistinctVaribale(query):
    distinct_variable = set()
    for q in query:
        for c in q:
            if c not in USER_OPERATOR:
                distinct_variable.add(c)
    return distinct_variable

# Method for generating Truth Table using backtracking: Return List of truth table
def generateTruthTable(n):
    result = []
    data = ['0','1']
    def backtrack(n,ans):
        if n==0:
            result.append(ans)
            return
        for i in data:
            backtrack(n-1,ans+i)
    backtrack(n,'')
    return result

# Method for building queries using and or: Return string (query)
def buildQuery(q):
    def convertToExpression(q):
        expression =''
        for e in q:
            if e not in USER_OPERATOR:
                expression = expression + e
            else:
                if e=='|':
                    expression = expression + ' ' + 'or' + ' '
                elif e=='&':
                    expression = expression + ' ' + 'and' + ' '
                elif e=='!':
                    expression = expression + ' ' + 'not' + ' '
                elif e=='=':
                    expression = expression + ' ' + '==' + ' '
                elif e=='(' or e==')':
                    expression = expression + ' ' + e + ' '
        return expression

    return convertToExpression(removeDoubleAndSingleImplication(q))

# Method for evaluting expression (Adding True or False to the queries): Return Query
def evaluteExpreesion(query,dic={},distinct_variable=[]):
    for i in range(len(query)):
        if query[i] in distinct_variable:
            temp = query[:i] + dic[query[i]] + query[i+1:]
            query = temp
    return eval(query)

# Method for converting queries to CNF: Return List of CNF's
def convertToCNF(quries):
    CNF =[]
    for query in quries:
        distinct_variable = list(findDistinctVaribale(query))
        # print("\n\nNumber of Distinct Variable :",distinct_variable)
        truth_table = generateTruthTable(len(distinct_variable))

        q = buildQuery(query)
        q_cnf =[]
        for table in truth_table:
            dic ={}
            for t in range(len(table)):
                dic[distinct_variable[t]] = table[t]
            if not evaluteExpreesion(q,dic,distinct_variable):
                cnf =[]
                for v in dic:
                    if dic[v]=='1':
                        cnf.append('not '+v)
                    else:
                        cnf.append(v)
                q_cnf.append(' or '.join(cnf))
                # print(q,evaluteExpreesion(q,dic,distinct_variable),query,' or '.join(cnf))
        CNF.append(q_cnf)
    return CNF

''' 
End Utilities function for Generating Truth Table 
and Evalute Expression. Convert it to CNF.
'''

''' 
Implement function for resolution-refutation.
'''
# Method for resolution-refutation: Return 1|0
def resolution(cnf,m):
    all_cnf = []
    for c in cnf:
       all_cnf += c
    claues = set(all_cnf)
    new = set()

    def resolvent(c1,c2):
        r_c1 = set(c1.split(' or '))
        r_c2 = set(c2.split(' or '))
        for i in c1.split(' or '):
            for j in c2.split(' or '):
                if (i=='not '+j) or ('not '+i==j):
                    r_c1.remove(i)
                    r_c2.remove(j)
                    temp = r_c1.union(r_c2)
                    if len(temp)>0:
                        return ' or '.join(temp)
                    else:
                        return ''
        
        temp = r_c1.union(r_c2)
        if len(temp)>0:
            return ' or '.join(temp)
        else:
            return ''
        return ' or '.join(temp)

    while True:
        for c1 in claues:
            for c2 in claues:
                res = resolvent(c1,c2)
                if res=="":
                    return 1
                new_res = set([res])
                # if m==1:
                #   print(new_res)
                new = new.union(new_res)
        if new.issubset(claues):
            return 0
        claues = claues.union(new)
        # break

''' 
End resolution-refutation.
'''

# Method to take input from the user
def takeInput():
    nm = list(map(int,input().split()))
    n,m = nm[0],nm[1]
    query = []
    for _ in range(n):
        query.append(input())
    toProve = input()
    return [query,toProve,m]

# Method to print CNF list
def printCNF(cnf_list):
    for cnf in cnf_list:
        print(cnf)

# Main function
def main():
    INPUT = takeInput()
    query = INPUT[0]
    toProve = INPUT[1]
    m = INPUT[2]
    '''
    # Sample hard code input 
    # query= ['P|(Q&(R>T))', 'P>R', 'Q>T', 'Q>(R=T)']
    # query =['Q>(R=T)']
    # toProve = 'R'
    '''
    
    # # Sample hard code input 2
    # query = ['(S&W)>E', '(W&P)>H', 'R>!H', 'R>G','W','R', 'S']
    # toProve = 'E'
    # n,m = 4, 1
    
    query.append('(!'+toProve+')')
    CNF_list = convertToCNF(query)
    # if m==1:
    #     printCNF(CNF_list)
    ans = resolution(CNF_list,m)
    print(ans)


if __name__=="__main__":
    main() 
