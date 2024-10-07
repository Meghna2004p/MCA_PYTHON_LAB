#include<stdio.h>
int main()
{	
	int a=3,b=2,result;
	result=a-b;
	printf("result is:%d",result);
	if(result<0)
	{
	printf("-ve number");
	}
	else
	{
	if(result>0)
	{
	printf("+ve number");
	}
	else
	{
	printf("zero");
	}
}
	return(0);
}
