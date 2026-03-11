n = int(input(' Enter the number of students: '))

for i in range(n):
 print(f'---------student-{i+1}-----------')
 name = input(' Enter the names: ')
 gpa = float(input(' Enter the CGPA: '))

 if gpa>max_val:
     max_name= name 
     max_val=gpa
     
 if gpa<max_val:
     max_name= name 
     max_val=gpa

 names.append(name)
 gpas.append(gpa)

print(f'{'names.ijust(15)}{'gpa'.ijust(5)}')