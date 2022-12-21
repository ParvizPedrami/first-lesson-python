import math

q1= input("please enter your first name:")
q2=input("please print your last name:")

a= float(input("Enter the score of the first exam: "))
b= float(input("Enter the score of the second exam: "))
c= float(input("enter the score of the third exam: "))

print("first name: ",q1,"\n last name: ", q2)

average= float((a+b+c)/3)
print ("average:", average)

if average>=17:
    print("Average status: GREAT")

if average <17 and average>=12:
    print("average status: NORMAL")

if average<12:
    print("average status: FAIL")

