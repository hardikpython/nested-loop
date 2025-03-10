name=str(input("enter your word"))
character=(input("enter your character"))
i=0
count=0
while(i<len(name)):
    if (name[i]==character ):
     count=count+1
    i=i+1
print(count)