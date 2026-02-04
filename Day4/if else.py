products = ['heels','shirts','handbags','laptops','facewash']
search = input('enter the item: ')

if search in products:
    print(f'{search} is found!\n go shop now!!!')
else :
    print(f'{search}is not found\n look for other things!!')