def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

exp = input('Enter the exp: ')

for i in exp:
    if i == '+':
        a,b=exp.split('+')
    elif i == '-':
        a,b=exp.split('-')
    elif i == '*':
        a,b=exp.split('*')
    elif i == '/':
        a,b=exp.split('/')
    elif i == '%':
        a,b=exp.split('%')