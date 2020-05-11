import hashlib
import json
from datetime import datetime


class Transaction():
    '''
    Transaction constructor takes argument: 
    from_address: {address or account of user who want to send money.},
    to_address: {address or account of user to whom want to send money.},
    amount: {ammount of the money.}
    '''
    def __init__(self,from_address,to_address,amount):
        self.from_address=from_address
        self.to_address=to_address
        self.amount=amount

class Block():
    '''
    Block: Constructor takes argument:
    tstamp: {time stamp},
    transactionsList: {Transaction class object},
    previousHash: {previous hash value}
    '''
    def __init__(self,tstamp,transactionsList,previousHash=''):
        self.nonce=0
        self.tstamp=tstamp
        self.transactionsList=transactionsList
        self.previousHash=previousHash
        self.hash=self.calculateHash()

    '''
    calculateHash: It returns the Hash value on the basis of nounce,tstamp,transactionsList's amount, and previous hash.
    '''
    def calculateHash(self):
        block_string=json.dumps({"nonce":self.nonce,"tstamp":str(self.tstamp),"transaciton":str(self.transactionsList),"previousHash":self.previousHash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    '''
    mineBlock: It restrict the user from adding block by having difficulty lavel(number of zeros start with hashValue).
    '''
    def mineBlock(self,diffic):
        while(self.hash[:diffic] != str('').zfill(diffic)):
            self.nonce += 1
            self.hash=self.calculateHash()
        print("Block mined ", self)
    def __str__(self):
        string="nonce: " + str(self.nonce) + "\n"
        string+= "tstamp: " + str(self.tstamp)+ "\n"
        string += "prevhas: " + str (self.previousHash)+ "\n"
        string += "hash: " + str (self.hash)+ "\n"
        return string

class BlockChain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]
        self.pendingTransations=[]
        self.mining_reward=100
        self.difficulty=3
    '''
    setTheDifficultyLavel
    '''
    def setTheDifficultyLavel(self,difficulty):
        self.difficulty=difficulty
    '''
    generateGenesisBlock: Generate the first block hash.
    '''
    def generateGenesisBlock(self):
        return Block('11/05/2020',[Transaction(None,None,0),])
    
    '''
    minePendingTransatin: add panding transaction(done by miner and get his reward).
    '''
    def minePendingTransatin(self,mining_reward_address):
        for pT in self.pendingTransations:
            from_add = pT.from_address
            to_add = pT.to_address
            ammount = pT.amount
            if from_add==to_add:
                print("Transaction failed: <same from address and to address>")
                continue
            # get_balance_from_add = self.getBalance(from_add)
            # is_Valid_to_add = self.isValidAdd(to_add)
            # if not is_Valid_to_add:
            #     print("Transaction failed: <Not valid address>")
            #     continue
            # if get_balance_from_add < ammount:
            #     print("Transaction failed: <Not sufficient balance>")
            #     continue
            previousHash = self.chain[-1].hash
            block = Block(datetime.now(),pT,previousHash)
            block.mineBlock(self.difficulty)
            self.chain.append(block)
        self.pendingTransations=[Transaction(None,mining_reward_address,self.mining_reward)]
        print("Block is mined. Reward ammount id ", self.mining_reward)

    '''
    createTransaction: Create a new Transaction and add this in pandending transaction completed when minor mines the block.
    '''
    def createTransaction(self,T):
        self.pendingTransations.append(T)
    '''
    getBalance: Return the balance of the specific user
    '''
    def getBalance(self,address):
        balance=0
        for b in self.chain:
            for t in b.transactionsList:
                if t.to_address == address:
                    balance += t.amount
                if t.from_address == address:
                    balance -= t.amount
        return balance 
    '''
    isChainValid: It checks if Block is valid or not means not modified by another user.
    '''
    def isChainValid(self):
        for i in range(1,len(self.chain)):
            prevb=self.chain[i-1]
            currb=self.chain[i]
            if(currb.hash != currb.calculateHash()):
                print("invalid block")
                return False
            if(currb.previousHash != prevb.hash):
                print("invalid chain")
                return False
        return True
    
    def isValidAdd(self,address):
        for b in self.chain:
            for t in b.transactionsList:
                if t.from_address==address:
                    return True
        return False

    def transactionHistory(self):
        print("Successful Transactions are: ")
        for c in self.chain:
            print(c)