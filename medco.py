a = (100*"*")
print(a)
b = "MEDCO"
c = b.center(90)
print(c)
print(a)

username = input("Enter your Username : ")
password = input("Enter your Password : ")

while len(password) < 8:
    print("Password should be at least 8 characters long")
    password = input("Enter your Password : ")
else:
    print("Password is valid")
print(f"Hello {username} how can i assist you sir?")

disease = input("do you have disease sir ?")
if disease == "yes" :
   disease_dict = {"cold" : "dolo650" , "cough" : "hot water" , "headache" : "sleep and "} # we use dictinory to store all our med problems and solutions
   problem = input("enter your problem :") # we input all med problems

   if problem in disease_dict:
    print(f"Problem: {problem} and your solution is {disease_dict[problem]}") #matching of problems and sloutions for dictionary takes places
   else:
    print(f"Sorry, no solution found for {problem}. Please try again.") #noting found says try again