password = input('Enter the password: ')

if len(password)>=8:
    s = set()
    for i in password:
        if i.isupper():
            s.add('upper')
        elif i.islower(): 
            s.add('lower')       
        elif i.isdigit(): 
            s.add('digit') 
        else:
            s.add('splchar')  
    if len(s)==4:
        print("strong password")
    else:
        print('weak password. strong password needs Upper,Lower,Digit,Splchar')
else:
    print('length need to be greater or equal to 8')        

