name = input('enter your name: ')
dob = input('enter your dob [YYYY-MM-DD]: ')

username = name[:2]+name[-2:]+dob[-2:]+dob[2:4]

print(f'hi {name} !\nYour username is: {username}')