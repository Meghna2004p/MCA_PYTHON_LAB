n=int(input("enter the number of terms:"))
a=0
b=1
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b