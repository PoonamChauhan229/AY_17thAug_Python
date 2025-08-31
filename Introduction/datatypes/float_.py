# whole numbers >> 0.2 >> 0 ||1 
# floating values >> 3.567890333333333333333333333333333333333 >>3.6 ||3.0 >> rounded off
# float
# decimal values
# pi >>3.14 >> scinetific values || constant values

a=34.5
print(a)
print(type(a))
print(22/7) # it doesnt round off

# 10 >> integer
# Make it as a float >> 10.0  

# 0 0.1 0.2 0.3....................................... 1
# 1 1.1 1.2 1.3....................................... 2


a="35.8"
print(type(a))
b=float(a)
print(b,type(b))


# x="this is float"
# y=float(x)
# z=int(x)
# print(y,type(y)) # output :could not convert string to float error
# print(z,type(z)) # output :invalid literal for int() error

# python encouters an error , it will stop the further execution

x1="30"
y1=float(x1)
z1=int(x1)
print(y1,type(y1)) # output :30.0 float
print(z1,type(z1)) # output :30  int

print("-----------------")

print(10/2) # output ? int || float  >>5.0
# fraction >>think >> o/p-integers >> python >>float  >> add .0

a=33.3333333333333 # 33.3
b=34.5222222222222 # 34.5
c=40.6333333333333 # 41.0

print("------round Method-----------")
# round() >> round(value,nos to round off)
# arguments >> round Methods 2 args
# 1st args is mandatory
# 2nd args is optional >> if i dont pass still it wont throw any error
print(a) 
t=round(a)  # 33  >> integer
print(t,type(t))
u=round(a,3) # 33.333  >> float 
print(u,type(u))

print("------round Method-----------")
print(b)
d=round(b)  # 1 args 
print(d,type(d))
g=round(b,2) # 2 args 
print(g,type(g))

# arguments >> short form >> args >> when u pass actual values to method
# print()  n args >> 1 args >>mandatory, more than 1 >>optional
# int()    1 args
# float()  1 args
# round()  2 args >> 1 >> mandatory , 2nd optional







