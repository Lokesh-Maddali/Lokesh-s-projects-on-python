kyc_documents={}
def check_balance():
    print(f"Your current balance is {balance}")
    print("*******************************")

def deposit(amount):
    global balance
    if amount >0:
        balance +=amount
    else:
        print("Invalid amount")
        print("*******************************")

def withdraw(amount):
    global balance
    if amount<0:
        print("Invalid amount")
        print("*******************************")
    elif amount > balance:
        print("Your balance is low")
        print("*******************************")
    else:
        balance -=amount

def kyc(**docs):
    global kyc_documents
    kyc_documents.update(docs)
    print("******************************************")

def check_kyc():
    if len(kyc_documents)==0:
        print("KYC is not done")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")
        print("**************************************")

balance = 0.0

if __name__=="__main__":
    print("**************************")
    print("Welcome to SHLJ Banking App")
    print("**************************")
    while True:
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5.Update KYC")
        print("6. Exit")
        choice=int(input("Enter your choice (1-6):"))
        print("*********************************")

        if choice== 1:
            check_balance()
        elif choice== 2:
            amt=float(input("Enter your amount to deposit:"))
            deposit(amt)
            print(f"Your current balance is {balance}")
        elif choice== 3:
            amt=float(input("Enter your amount to withdraw:"))
            withdraw(amt)
            print(f"Your current balance is {balance}")
        elif choice== 6:
            print("Quiting ,have a nice day")
        elif choice== 5:
            check_kyc()
        elif choice== 4:
            docs={}
            documents=int(input("Enter the number of documents you want to add"))
            for i in range(documents):
               key= input("Enter the document type:")
               value= input("Enter the document number :")
               docs[key]=value



            break
        else:
            print("Invalid choice")
            print("*******************************")

    print("Thank you for banking with us!!!")
