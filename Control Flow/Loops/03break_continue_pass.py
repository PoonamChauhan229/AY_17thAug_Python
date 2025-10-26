# break , continue ,pass 
# while /for
# break    >>exit the loop
# continue >>skip the current iteration
# pass >>  Does nothing >> u can replce at block of code

# for loop >> break

# 1-5
for i in range(1,6):
    if(i==1):
        print(i,"You are allowed")
    elif(i==2):
        print(i,"Not allowed")
        break
    elif(i==3):
        print(i,"Not allowed-2")
    else :
        print(i)
print("while loop")
start=1
while start<6:
    if(start==1):
        print(start,"You are allowed")
    elif(start==2):
        print(start,"Not allowed")
        break
    elif(start==3):
        print(start,"Not allowed")
    else :
        print(start)
    start+=1

print("continue")
for i in range(1,6): #12345
    if(i==1):
        print(i,"You are allowed")
    elif(i==2): 
        continue
        print(i,"Not allowed")
    elif(i==3):
        print(i,"Not allowed")
    else :
        print(i)

print("while loop")
count=1
while count<6:
    if(count==1):
        print(count,"You are allowed")
    elif(count==2):
        count+=1 #>> increment+ skip
        continue #skips the current iteration >> cannot increment by itself
    elif(count==3):
        print(count,"Not allowed")
    else :
        print(count)
    count+=1 #2

# pass
for i in range(45,47):
    pass #dont do anything

if (8<10):
    pass
    
# project >> calculator
print("-----------Calculator------------")
num1=float(input("Enter the 1st num : "))
op=input("Enter the operator +,-,*,%,/ : ")
num2=float(input("Enter the 2nd number : "))
print(num1,op,num2)

if op=="+":
    print("+ Operator ", num1+op+num2)
elif op=="-":
    pass
else:
    pass

#pass >> u are thiinking abt logic , no errors needed
#pass >> write rest of code , and then come do the logical part above>> wrote now , but usage is later , i write it later , i might forget
# create the structure
