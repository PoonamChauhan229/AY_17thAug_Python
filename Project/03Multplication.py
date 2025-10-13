# 5 * 1 = 5
# 5 * 2 = 10......

# for i in range(5,51,5):
#     print(i)

# 13 table
# 25 table
# 79 table

# 2*1 =2  ||| 79 *1 =79 ||| 25 *1=25
# 79 *10 =790
# start 79 end 791 step 79

print("-------------")
# for i in range(79,791,79):
#     print(i)

print("-------------")
# 25 *10 =250
# for i in range(25,251,25):
#     print(i) #print 

# Not an ideal approach

# Aprroach >> Ideal >>
num=79  # 1 >> 10 >> 5 *1 =5 to 5*10=50 # user wants
for i in range(1,11,1):
    print(num,"*",i,"=",num*i)

number=int(input("Enter the number of which Multiplication You want :"))  # 1 >> 10 >> 5 *1 =5 to 5*10=50 # user wants
for i in range(1,11,1):
    print(number,"*",i,"=",number*i)
