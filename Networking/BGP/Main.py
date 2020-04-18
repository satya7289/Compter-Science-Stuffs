import collections
from collections import defaultdict 

def myfun():
    FILE_NAME = "bgp-routing-table.txt"

    file = open(FILE_NAME,'r')

    UNIQUE_AES = set([])
    IP_PREFIX = set([])
    ROUTING_TABLE = set([])
    ISP = set([])
    DICT = defaultdict(set)

    counter = 0
    for i in file:
        temp = i.split("|")
        prefix = temp[5]
        as_path= temp[6]

        # Question 1.
        IP_PREFIX.add(prefix)
        for j in as_path.split(" "):
            UNIQUE_AES.add(j)
        
        # Question 2. First part
        sub_net = prefix.split("/")[1]
        if prefix.startswith(("103.21.124.","103.21.125.","103.21.126.","103.21.127.")) and sub_net=="24":
            ROUTING_TABLE.add(prefix+" "+as_path)
        

        # Question 4.
        as_path_list = as_path.split(" ")
        AS  = as_path_list[-1]
        DICT[AS].add(as_path_list[as_path_list.index(AS)-1])

        counter += 1
        # if counter==1000:
        #     break
        print(counter,"..")

    file.close()

    # Question 1. printing part
    print("First Question...")
    print(". Number of IP prefixes are: ", len(IP_PREFIX))
    print(". Number of Unique AES are: ", len(UNIQUE_AES))
    print("\n---------------------")

    # Question 2. Printing part
    print("Second Question...")
    print("IP prefix and AS Path for Inst-1")
    for table in ROUTING_TABLE:
        print(table)
    print("\n---------------------")

    # Question 3.
    INST_AES = None
    for a in ROUTING_TABLE:
        aes = a.split(" ")
        INST_AES= aes[-1]
        ISP.add(aes[aes.index(INST_AES)-1])
        
    print("Third Question...")
    print(". Total ISP provider for Inst-1 are", len(ISP))
    print(". ISP are: ", ISP)
    print(". Inst-1 AES: ",INST_AES)
    print("\n----------------------")

    # Question 4. Printing part
    print("Fourth Question...")
    print("Top 10 ISP are: ")
    L= []
    for i in DICT:
        L.append((len(DICT[i]),i))
    L.sort(reverse=True)
    TOP_ISP = L[0:10]
    for isp in TOP_ISP:
        print(".", isp[1], "having connection ",isp[0])
    
            
if __name__=="__main__":
    myfun()







