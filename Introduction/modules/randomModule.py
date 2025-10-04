# use the methods /properties of that package
# packageName.method()|| packageName.property
import random

# print(random.random()) #0 - 1.0 >> float

# print(random.uniform(10,20)) #10-20 , 10 & 20 included >>float

# print(random.randint(10,20)) #10-20 , 10 & 20 included >>integer

# random.randrange() 
# print(random.randrange(5,10)) #5-10 , 10 & 20 included >>integer
# print(random.randrange(5,10,1)) #5-10 , 10 & 20 included >>integer
#step >> skip 
# 5 7 9 11
# 5 10
# 5 7 9

# 1. Write a program that simulates the flipping of a coin. Indicate whether the coin has landed as heads or tails.

# select the choice >>" " ,[]
coin=random.choice(["Head","Tail"])
print("flipping of a coin: ",coin)


# 2. Write a program that randomly generates 4 marks out of 100. Output the marks and the mean average and determine whether the average is an honours, a fail, or a pass with an appropriate message

num1=random.randint(0,100)
num2=random.randint(0,100)
num3=random.randint(0,100)
num4=random.randint(0,100)

# print(num1,num2,num3,num4)
avg=(num1+num2+num3+num4)/4
# print(avg)

if avg>=70:
    print("Honours: You scored:",avg)
elif avg>=45:
    print("Pass: You scored:",avg)
else:
    print("Fail: You scored:",avg)

# 3. Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random, each time the program is run.

fortuneList=["fortune1","fortune2","fortune3","fortune4"]
uniqueFortune=random.choice(fortuneList)
print(uniqueFortune)

# Write a program that simulates the rolling of a die. The program will output the number rolled   along with a picture of the die using ASCII characters.
# 1-6 >> choice >>string >>int >> 
diceRolled=random.randint(1,6)
print("You rolled a dice and number is :",diceRolled)



