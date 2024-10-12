x=input("enter a string: ")
count=0
for i in x:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
print("the number of vowels in string are: ",count)