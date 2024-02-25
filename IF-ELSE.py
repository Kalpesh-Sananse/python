#ifelse

print("Ener your marks")
number = int( input())
print(number)


if(number > 90 and number<100):
    grade = 'A'
elif (number>80 and number<100):
    grade = 'B'
else:
    grade = "dont know"

print("the grade is ",grade)