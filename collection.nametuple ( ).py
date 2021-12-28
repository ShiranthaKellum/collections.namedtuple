
noOfStudents = int (input ())
student = list (input ().split ())
total = 0
for i in range (noOfStudents):
    total =+ int (list (input ().split ()) [student.index ('MARKS')])

print (total/noOfStudents)