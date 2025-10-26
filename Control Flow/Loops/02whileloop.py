# start , stop >> condition
# direct values >> put a number/value to stop
# compute , get some specific output >> condition to stop

# for in loop >> start stop , step (optional) || default step takes 1
# for _ in range():

# while loop
# while condition:
    # block of code
# 50-70
# start-missing 
# stop-condition-Present ,
#  step >(optional) |||| default step takes 1 >>misisng
# 50-70          -Ques1
# 50,52....70    -Ques2
print("50-70")
start=50
while start <71:
    print(start)
    # start=start+1
    start+=1
# start =50 , loop >> 50<71 >> True always
# increase step 


# val >> 0 and terminate >> 5  >> Print 0 1 2 3 4

print("19th October")
for i in range(0,5,1):
    print(i)

print("while loop")
# while condition >> stop >>>> Print 0 1 2 3 4
count =0 # start point >>
while count <5:
    print(count)
    count=count+1

# count = 0  || count<5 >>0<5>> T  ||print count >>0 ||  count=count+1 >>0+1 >>1 >>count=1
# count = 1  || count<5 >>1<5>> T  ||print count >>1 ||  count=count+1 >>1+1 >>2 >>count=2
# count = 2  || count<5 >>2<5>> T  ||print count >>2 ||  count=count+1 >>2+1 >>3 >>count=3
# count = 3  || count<5 >>3<5>> T  ||print count >>3 ||  count=count+1 >>3+1 >>4 >>count=4
# count = 4  || count<5 >>4<5>> T  ||print count >>4 ||  count=count+1 >>4+1 >>5 >>count=5   
# count = 5  || count<5 >>5<5>>F   ||loop terminate/stop >> execution end
# 0
# 1
# 2
# 3
# 4

# indentation is very very important 

print("while loop2")
# while condition >> stop >>>> Print 0 1 2 3 4
count =0 # start point >>
while count <5:
    print(count)
    count+=1 # learnt assignmnet seperatly >> using it >> apply 

# loops , conidtional statements (if , if else if elif .....else)
# loop +if 

print("loops _if 1")
# for in
for i in range(20,25): #20 21 22 23 24
    # print("Prnt all i values",i)
    if(i==23):
        print(i,"You are allowed") 
    elif(i==24):
        print(i,"You need to pay 500, then allowed")
    else:
        print(i,"Access Denied")


print("new while and if")
start=20
while start<25: #20 21 22 23 24
    if(start==23):
        print(start,"You are allowed") 
    elif(start==24):
        print(start,"You need to pay 500, then allowed")
    else:
        print(start,"Access Denied")
    start+=1







    
   

    

