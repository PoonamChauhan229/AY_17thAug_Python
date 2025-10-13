# in      >> True >>if exists 
# not in  >>True >> if not exits
# O/p >>True False


a=[1,2,3]
# 2 is existing ?

print(2 in a) #True
print(4 in a) #False

# not in 
print(4 not in a) #True
print(2 not in a) #False

#identity operators >> ?
# O/p >>True False
x=10
y=10
# print(x==y) # true
# find out id in the memoey
# id()
print(id(x)) #140714980570312
print(id(y)) #140714980570312


a=67
b=a
print(id(a)) #140714980572136
print(id(b)) #140714980572136


# is 
# is not

print("--------------")
print(a is b)
print(x is y)

t="34"
q=34
print(t==q) #False
print(id(t)) 
print(id(q)) 

print("--------------")
print(a is not b)
print(x is not y)
print(t is not q)