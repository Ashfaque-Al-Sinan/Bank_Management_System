import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
                    
    except Exception as err:
        print(f"an exception occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __account_gen(cls):
        alpha=random.choices(string.ascii_letters,k=3) 
        num=random.choices(string.digits,k=3)
        specialchar=random.choices("@#$%&",k=1)
        id=alpha + num + specialchar 
        random.shuffle(id)
        return "".join(id)      
                        
    def CreateAccount(self):
        data={
            "Name" : input("tell your name :- "),
            "Age" :int(input("tell your Age:- ")),
            "Email":input("Tell your email:- "),
            "Pin":int(input("tell your 4 number pin:- ")),
            "Account_no":Bank.__account_gen(),
            "balance":0
        }
        
        if data['Age'] < 18 or len(str(data['Pin'])) != 4 :
            print("sorry you cannot create your account")
        else:
            print("account has ber created successfully")
            for i in data:
                print(f"{i}:{data[i]}")
            print("Please note down your account number")
            Bank.data.append(data)
            Bank.__update()        
    
    def deposit(self):
        acc_number=input("plz tell your account number: ")
        pin= int(input("plz tell your pin please : "))
        
        # Convert Account_no to string for comparison
        userdata=[i for i in Bank.data if str(i['Account_no'])==acc_number and int(i['Pin'])==pin]
        
        if len(userdata)==0:
            print("No Data Found")
        else:
            amount = int(input("how Much you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Print The amount is too Much plz deposit below 10k and above 0 ")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update() 
                print("amount deposited successfully")
    
    def withdraw(self):
        acc_number=input("plz tell your account number: ")
        pin= int(input("plz tell your pin please : "))
        
        # Convert Account_no to string for comparison
        userdata=[i for i in Bank.data if str(i['Account_no'])==acc_number and int(i['Pin'])==pin]
        
        if len(userdata)==0:
            print("No Data Found")
        else:
            amount = int(input("how Much you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("you cannot withdraw")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update() 
                print("amount Withdrew successfully")               
    
    def showdetails(self):
        acc_number=input("plz tell your account number: ")
        pin= int(input("plz tell your pin please : "))
        
        # Convert Account_no to string for comparison
        userdata=[i for i in Bank.data if str(i['Account_no'])==acc_number and int(i['Pin'])==pin]
        print("Your Informations are : \n\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
    
    def updateDetails(self):
        acc_number=input("plz tell your account number: ")
        pin= int(input("plz tell your pin please : "))
        
        # Convert Account_no to string for comparison
        userdata=[i for i in Bank.data if str(i['Account_no'])==acc_number and int(i['Pin'])==pin]
        
        if len(userdata)==0:
            print("no such user found")
        else:
            print("You Cannot Change The Age , Account ,Balance")
            print("Fill The Details for Change or leave it empty if no Change")
            
            newdata={
                "Name" : input("please tell new name : "),
                "Email" : input("New Email: "),
                "Pin"   :input("enter new pin: ")
            }
            
            # FIXED: Use assignment (=) instead of comparison (==)
            if newdata['Name'] == "" :
                newdata['Name'] = userdata[0]['Name']  # Fixed
            if newdata['Email'] == "":
                newdata['Email'] = userdata[0]['Email']  # Fixed
            if newdata['Pin'] == "":
                newdata['Pin'] = userdata[0]['Pin']  # Fixed
            
            newdata['Age'] = userdata[0]['Age'] 
            newdata['Account_no'] = userdata[0]['Account_no'] 
            newdata['balance'] = userdata[0]['balance']
            
            # FIXED: Convert PIN to int if it's a string
            if isinstance(newdata['Pin'], str) and newdata['Pin'].isdigit():
                newdata['Pin'] = int(newdata['Pin'])
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("Details Updated SuccessFully") 
    
    def Delete(self):
        acc_number=input("plz tell your account number: ")
        pin= int(input("plz tell your pin please : "))
        
        # Convert Account_no to string for comparison
        userdata=[i for i in Bank.data if str(i['Account_no'])==acc_number and int(i['Pin'])==pin]
        
        if len(userdata) == 0:
            print("sorry no such data exists")
        else:
            check= input("Press Y if you want to delete account or press n : ") 
            if check == "n" or check =="N" :
                pass
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Deleted Successfully")
                Bank.__update()   


user=Bank()
while(True):
    print("press 1 for creating an account")
    print("press 2 for Depositing Money in the Bank")
    print("press 3 withdrawing the Money")
    print("press 4 for details")
    print("press 5 for updating the details")
    print("press 6 for deleting your account")

    check= int(input("Tell your Response :-"))

    if check == 1 :
        user.CreateAccount()
        
    if check == 2 :
        user.deposit()
        
    if check == 3:
        user.withdraw()

    if check == 4 :
        user.showdetails()

    if check == 5 :
        user.updateDetails() 

    if check == 6 :
        user.Delete()