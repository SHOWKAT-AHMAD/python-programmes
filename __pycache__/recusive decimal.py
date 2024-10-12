n=input("enter a binary number: ").replace(" ","")
def convertToDecimal(x):
    if len(x)==0:
        return 0
    return 2**(len(x)-1)*int(x[0])+convertToDecimal(x[1:])

print("the binary number is equal to: ",convertToDecimal(n))