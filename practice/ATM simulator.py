balance = 10000
transactions ='0'

while True:
    print('/n ...ATM MENU...')
    print('1. chack balance')
    print('2. deposite')
    print('3. withdraw')
    print('4. exit')
    
    choice = int(input('enter your choice: '))

    if choice == 1:
        print('your balance is:',balance)

    elif choice ==2:
         amount = int(input('Enter your deposite amout: '))  
         if amount >= 0:
             balance += amount
             transactions += '1'
             print('deposite successful')

    elif choice ==3:
         amount = int(input('Enter your withdral amout: '))  
         if amount <= 0:
             print('invalid amount')
         elif amount > balance:
             print('insufficient balance')
         else:     
             balance -= amount
             transactions += '1'
             print('withdral successful')        

    elif choice == 4:
        print('exiting ATM')
        print('final balance:',balance)
        print('total transactions:',transactions)
        break
    else:
        print('invalid choice.try again.')