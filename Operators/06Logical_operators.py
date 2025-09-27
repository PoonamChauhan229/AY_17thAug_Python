# Logical Operator
# and
# or 
# not 

# and 
# 2 operations ||| == ,> ,<,<=,>=

# 2==2 True
# 2>6  False

# T T >>T  >> and 
# F T >>F

print(2==2 and 10>5) #T and T >>T
print(2==2 and 2>5) #T and F >>F
print(4==2 and 10>5) #F and T >>F
print(4==2 and 10>15) #F and F >>F 

print("--------------")
# or
print(2==2 or 10>5) #T or T >>T
print(2==2 or 2>5)  #T or F >>T
print(4==2 or 10>5) #F or T >>T
print(4==2 and 10>15) #F and F >>F 

print("--------------")

# not() >> reverse the reult
print(not(2==2 or 10>5)) #T or T >>T
print(not(1>4)) #>> False 

# if  poonam come  >>session ok
# if amulaya comes >>session ok

# if statement

# if(condition):
#     print("No access")

# if condition:
#     print("No access")

# age >> you are adult || you are senior || you are kid
age=5

if age>=21:
    print("You are an adult")

# if  1 condtion (True)>> o/p
# it fails >> who will handle
# 
# if else statemnt
# if condition:
#   block of code 
# else:
    # block of code

marks=50
if marks<35:
    print("Not elgible to go in next class")
else:
    print("Will come next year in same class")

# if elif elif elif  else
# elif else if 

# 1 condition ?? if else || if 
# more than 1 condition (3)>>to be tested/evaluted
# if condition:
#     block of code
# elif condistion:
#      block of code
# elif conidtion:
#     block of code
# else:
    # block of code

totalMarks=0  # 10 students >> Grade 
# >=90 >> Grade A
# >=75 >>Grade B
# >=50 >>Grade C
# default output >> Fail

if totalMarks>=90:
    print("Grade A")
elif totalMarks>=75:
    print("Grade B")
elif totalMarks>=50:
    print("Grade C")
else:
    print("Grade:Fail")
print("--------------")

# username , password >> login

# if username is incorrect >> login failed
# if password is incorrect >> login failed
# if username and password is correct  >> successful login

username="amulaya123"
password=1234

# if username and password is correct  >> successful login
if username=="amulaya" and password==1234:
    print("Succesful Login")
else:
    print("Login Failed")

# Red >Stop , Green >Go, Yellow >>Get Ready
signal="pink"

if signal=="green":
    print(">Get Ready")
elif signal=="red":
    print("Stop")
elif signal=="green":
    print("Go")
else:
    print("Unkonwn color")








