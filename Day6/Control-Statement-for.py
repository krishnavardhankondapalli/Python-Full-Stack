'''
for var in seq:
   stmts

seq: list,tuple,set,dict,str,range
'''



"List"

products = ['bread','butter','milk','suger','salt']

for product in products:
    print(f'{product} - add to fav | buy now | add to cart')

\

"Tuple"

sizes = ('xs','s','m','l','xl','xxl','xxxl')

for s in sizes:
 print(f'...|s|...')



"Set"

followers = {'archana','suhaan','hari','pandu','skn','kalyani'}

for i in followers:
   print(f'{i} - |follow back|remove|message|')



"Dictionary"

data = {
   "archana":['c','c++','python','java'],
   "suhaan":['1st grade','2nd grade','3rd grade'],
   "hari":['c','c++','java'],
   "pandu":['java','python','c']
}

for i in data:
   print(f"{i}: {data[i]}")




"string"

s = {'krishna vardhan'}

for i in s:
  print(f'{s}')



"range"

#range(start,stop+1,step) = range(0,n,1)
for i in range(1,101):
   print(i)



#range(start,stop+1,step) = range(0,n,1)
for i in range(2,101,2):
   print(i)



"table"

#range(start,stop+1,step) = range(0,n,1)
n = int(input('Enter the number: '))

print(f'{n}-table')
for i in range(1,11):
   print(f'{n}*{i}={n*i}')



"Break"

for i in range(1,11):
   if i==8:
      break
   print(i)



"Continue"

for i in range(1,11):
   if i==8:
      continue
   print(i)

