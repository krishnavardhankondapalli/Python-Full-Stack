data={
'sathvik':{ 'status':True, 'python':100, 'mysql':99, 'softskills':85},
'ravi': { 'status':False, 'python':40, 'mysql':50, 'softskills':None},
'dileep':{ 'status':True, 'python':50, 'mysql':28, 'softskills':32},
'praveen': { 'status':True, 'python':10, 'mysql':20, 'softskills':90},
'saaketh': { 'status':True, 'python':18, 'mysql':46, 'softskills':6},
}

user = input("Enter the student name: ")

if user in data:
    if data[user]['status']:
        sum = data[user]['python']+data[user]['mysql']+data[user]['softskills']+data[user]
        avg = sum/3
        if avg > 80:
            print(f"Congrats {user} !!!/nYou got 'A' grade")
        if avg > 60:
            print(f"Better luck {user} !!!/nYou got 'B' grade")
        if avg > 40:
            print(f"Need Improvement {user} !!!/nYou got 'C' grade")
        else:
            print(f"{user} Failed in the exam.\nBring your parents")

    else:
        print(f"{user} didn't write any exams.")
else:
    print(f"{user} not found")