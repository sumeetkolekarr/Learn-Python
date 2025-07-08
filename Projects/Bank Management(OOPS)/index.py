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
            print('No Such File Exists')
    except Exception as e:
        print(f'An exception occurred as {e}')
    
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices('!@#$%^&*', k=1)
        id = alpha + num +spchar 
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self):
        info = {
            'name': input('Tell your name: '),
            'age': int(input('Tell your age: ')),
            'email': input('Tell your email: '),
            'pin': int(input('Tell your pin: ')),
            'accountNo': Bank.__accountGenerate(),
            'balance': 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print('Sorry, You can not create your Account...') 
        else:
            print('Account has been created Successfully!') 
            for i in info:
                print(f'{i}:{info[i]}')
            print('Please Note Down your Account Number')
            Bank.data.append(info)
            Bank.__update()
    
    def depositMoney(self):
        accnum = input('Enter your Account Number: ')
        pin = int(input('Enter your Pin Number: '))
        
        userData = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        if userData == False:
            print('Sorry, No data Found')
        else: 
            amount = int(input('Enter Money to Deposit: '))
            if amount > 10000:
                print('Sorry, the amount is too much as you can deposit below 10000 and above 0')
            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print('Money Deposited Successfully')
    
    def withdrawMoney(self):
        accnum = input('Enter your Account Number: ')
        pin = int(input('Enter your Pin Number: '))
        
        userData = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        if userData == False:
            print('Sorry, No data Found')
        else: 
            amount = int(input('Enter Money to Withdraw: '))
            if userData[0]['balance'] < amount:
                print('Sorry, You dont have that much money!')
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print('Money WithDrew Successfully')
    
    def showDetails(self):
        accnum = input('Enter your Account Number: ')
        pin = int(input('Enter your Pin Number: '))
        userData = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        print('Your info is \n\n')
        for i in userData[0]:
            print(f'{i}:{userData[0][i]}')
    
    def updateDetails(self):
        accnum = input('Enter your Account Number: ')
        pin = int(input('Enter your Pin Number: '))
        
        userData = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        if userData == False:
            print('No Such Data Found')
        else:
            print('You can not change the age, account number and balance')
            print('Fill the details for change or leave it empty if no change')
            
            newData = {
                'name': input('Please Enter New Name or Press Enter: '),
                'email': input('Please Enter New Email or Press Enter: '),
                'pin': input('Please Enter New Pin or Press Enter: '),
            }
            
            if newData['name'] == '':
                newData['name'] = userData[0]['name']
            if newData['email'] == '':
                newData['email'] = userData[0]['email']
            if newData['pin'] == '':
                newData['pin'] = userData[0]['pin']
            newData['age'] = userData[0]['age']
            newData['accountNo'] = userData[0]['accountNo']
            newData['balance'] = userData[0]['balance']
            if type(newData['pin']) == str:
                newData['pin'] = int(newData['pin'])
            for i in newData:
                if newData(i) == userData(0)[i]
                    continue
                else:
                    userData[0][i] = userData[i]
            Bank.__update()
            print('Details Updated Successfully!')
    
    def delete():
        accnum = input('Enter your Account Number: ')
        pin = int(input('Enter your Pin Number: '))
        
        userData = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        if userData == False:
            print('Sorry, No such data Exists!')
        else:
            check = input('Press Y if you actually want to delete the account or Press N to exit the process')
            if check == 'n' or check == 'N':
                print('No Account is Deleted')
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                Bank.__update()
                print('Account Data Deleted Successfully')
user = Bank()

print('Press 1 for Account Creation') 
print('Press 2 for Money Deposition') 
print('Press 3 for Money Withdraw') 
print('Press 4 for Details') 
print('Press 5 for Details Update') 
print('Press 6 for Account Deletion') 

check = int(input('Tell your Response: '))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.delete()