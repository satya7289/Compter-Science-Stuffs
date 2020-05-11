from block import Block
from block import BlockChain
from block import Transaction


if __name__=="__main__":
    print("-------------------Simple Bank Transaction Block Chain-----------------------------")
    bank = BlockChain()
    while(True):
        print("1. Send Money")
        print("2. Mine Now")
        print("3. Check Account")
        print("4. All Transaction.")
        print("5. Exits")
        try:
            choice=int(input())
            if choice==1:
                from_add = input("Enter your account/address. ")
                to_add = input("Enter account whom you want to send money. ")
                ammount = int(input("Enter the ammount: "))
                bank.createTransaction(Transaction(from_add,to_add,ammount))
                print("Thank you. Your Transaction is created..")
                print("__________________________________")
            elif choice==2:
                your_add = input("Enter your account/address. ")
                bank.minePendingTransatin(your_add)
                print("Thankyou you will get credted for mining reward soon..")
                print("___________________________________")
            elif choice==3:
                your_add = input("Enter your account/address. ")
                print(your_add, " current balance is ", bank.getBalance(your_add))
                print("___________________________________")
            elif choice==4:
                bank.transactionHistory()
            elif choice==5:
                break
            else:
                print("Enter correct choice..")
        except ValueError:
            print("Enter correct choice..")
 