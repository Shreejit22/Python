A1=int(input("Enter marks of subject 1"))
A2=int(input("Enter marks of subject 2"))
A3=int(input("Enter marks of subject 3"))
A4=int(input("Enter marks of subject 4"))
A5=int(input("Enter marks of subject 5"))
A6=int(input("Enter marks of subject 6"))
A=A1+A2+A3+A4+A5+A6
Percentage=(A/600)*100
print("Percentage is: ",Percentage)
if Percentage<35:
      print("Failure")
elif Percentage>=35 and Percentage<50:
      print("Passed")
elif Percentage>50 and Percentage<60:
      print("Second Division")
elif Percentage>60 and Percentage<70:
      print("third Division")
else:
      print("First class with Distinction")
      

      
