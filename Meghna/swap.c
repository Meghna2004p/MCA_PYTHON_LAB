#include<stdio.h>
int main()
{
	int num1=20,num2=50,temp;
	printf("two numbers num1=%d,num2=%d",num1,num2);
	temp=num1;
	num1=num2;
	num2=temp;
	printf("After swapping num1=%d,num2=%d",num1,num2);
}
