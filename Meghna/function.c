#include<stdio.h>
int sum(int,int);
int main()
{
	int num1=10;
	int num2=20;
	int result;
	result=sum(num1,num2);
	printf("%d",result);
	return(0);
}
	int sum(int num1,int num2)
{
	int result;
	result=num1+num2;
	return(result);
}
