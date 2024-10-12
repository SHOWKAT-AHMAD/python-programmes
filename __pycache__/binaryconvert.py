n=input("enter a binary number: ").replace(" ","")
decimal=0
for i in range(0,len(n)):
       decimal+=(2**(len(n)-1-i))*int(n[i])
print("the binary number is equal to: ",decimal)  
 