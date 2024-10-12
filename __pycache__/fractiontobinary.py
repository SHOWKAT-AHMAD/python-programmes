n=float(input("enter a fractional number: " ))
interger_part=int(n)
fractional_part=n-interger_part
def intergerdecimal(m):
    result=""
    while m > 0:
        r = m % 2
        result=str(r)+result
        m//=2
    return result  

def fractional_decimal(m,y):
    result=""
    while m >0 and len(result) <10:
        m*=2
        result+=str(int(m))
        m-=int(m)
    return result
      
firstbinary=intergerdecimal(interger_part)
secondbinary=fractional_decimal(fractional_part,10)
binary=firstbinary +"."+secondbinary
print("the binary of float number is: ",binary)
      