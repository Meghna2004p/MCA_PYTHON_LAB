a=[]
n=int(input("enter the no of elements in list:"))
for x in range(0,n):
    element=input("enter the elements" +str(x+1)+":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i))>max1:
        max1=len(i)
        temp=i
print("the word with longest length:")
print(temp)
