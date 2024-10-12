n=input("enter a string: ")
sum=0
count=0
for i in n:
    if i.isdigit():
         sum+=int(i)
         count+=1
    else:
         sum=sum     
print(sum)
print(sum/count)         