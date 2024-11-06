student={
'name':input("enter the student name:"),
'roll no':input("enter the roll no:"),
'reg no':input("enter students reg no:"),
'dept':input("enter students departement:"),
'sem':input("enter students semester:"),
}
print("entered students details:",student)
total_mark=int(input("enter the students total mark:"))
student['total_mark']=total_mark
if total_mark>=90:
    grade='A'
elif total_mark>=82:
    grade='B'
elif total_mark>=75:
    grade='c'
elif total_mark>=60:
    grade='D'
elif total_mark>=50:
    grade='pass'
else:
    grade='f'
student['grade']=grade
print("\n updated students details:",student)
del student['roll no']
print("\n students details after deletion:",student)
