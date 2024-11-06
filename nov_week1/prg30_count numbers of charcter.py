string=input("enter the string")
for i in string:
    freequency=string.count(i)
    print(str(i)+":"+str(freequency),end=",")
