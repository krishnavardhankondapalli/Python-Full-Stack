name = input('Enter your name: ')
mobile_number = int(input('Enter your mobile number: '))
product_1 = input('Enter your product 1: ')
price_1= float(input('Enter your product 1 price 1: '))
product_2 = input('Enter your product 2: ')
price_2= float(input('Enter your product 2 price 2: '))
product_3 = input('Enter your product 3: ')
price_3= float(input('Enter your product 3 price 3: '))

print (f'{name } your bill')
print(f'{product_1}; ${price_1}')
print(f'{product_2}; ${price_2}')
print(f'{product_3}; ${price_3}')

totaL_Bill = price_1+price_2+price_3

print(f'total_Bill: ${totaL_Bill}')

print('thank you')
