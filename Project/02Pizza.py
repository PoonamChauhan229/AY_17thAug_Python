pizzaPrice=15
toppingsNumber=int(input("Enter the toppings:")) # int()>> input returns string
print(toppingsNumber)
toppingPrice1=1.50
toppingPrice2=1.25

if toppingsNumber <=3:
    print("FinalPrice",(toppingPrice1*toppingsNumber)+pizzaPrice)
else:
    print("FinalPrice", (toppingPrice1*3)+(toppingPrice2*(toppingsNumber-3))+pizzaPrice)

    # 3 >>1.50
    # 4 >> 1.50*3+1.25 || 4-3>>1 >>1.25
    # 5 >> 1.50*3  + 1.25 +1.25 || 5-3 >>2
    # 
