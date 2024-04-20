print("hello")
input("whats the name?  ")
a=input("how are you ? Say it in-Fantastic and bad = ")
if a=="Fantastic":
      print("Its good to listen")
else:
      print("ohhh, shall i make your day good")
input("which branch = ")
print("cool" +" "+input("first sem SGPA=")+" "+ "good")
print("want to calculate CGPA  ")
a=input("enter yes or no = ")
if a=="yes":
      print("ok good, go forward")
else:
      print("ok thanks for the information")
SGPA=input("enter your SGPA = ")
Credits=input("enter your credits = ")
total=float(SGPA)*int(Credits)
print("Total sum of",total )
total_Credits_earned=int(input("enter total credits earned = "))
CGPA=(total)/(total_Credits_earned)
print(" Your CGPA Is",CGPA)
