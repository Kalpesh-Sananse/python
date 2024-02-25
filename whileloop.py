 #while loops

print("enter a number")
number = int (input())

while(number>4):
    print("number is greater than 4")
    number = int(input())
    if(number == 8):
         break
    if (number == 7):
         continue
    print("loop ended")