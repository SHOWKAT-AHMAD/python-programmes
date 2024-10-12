p=int(input("enter the price: "))
d=int(input("enter the discount: "))

def calculatePrice(x,y=10):
    return x-x*y/100
if d==0:
    print("the final price is: ",calculatePrice(p))
else:
    print("the final price is: ",calculatePrice(p,d))
