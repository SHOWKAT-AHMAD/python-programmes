n=input("enter a number: ")
m=input("chose 'hexa' or 'octa' you want to convert to: ").lower()
def convertNumber(x,y):
    result=""
    if m=="octa":
        while x!=0:
            q=int(x)%8
            result+=str(q)
            x=int(x)/8
    else:
        while x!=0:
            q=int(x)%16
            if q < 10:
               result+=str(q)
            else:
                result+=chr(q-10+ord('A'))   
            x=int(x)/16
    return result          
print("the answer is: ",convertNumber(n,m))
