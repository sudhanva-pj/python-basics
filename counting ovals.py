
text=input("enter any text:")
count=0
for i in text:
    if i in "aeiou AEIOU":
        count+=1
print ("there are",count)