def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
num=int(input("enter the no:"))
if num<0:
    print("enter a positive integer")
else:
    print("fibbonacci sequence:")
    for i in range(num):
        print(fibo(i))
