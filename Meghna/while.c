#include<stdio.h>
int main()
{
	int i=1;
	int sum=0;
	while(i<=10)
	{
		sum=sum+i;
		i=i+1;
	}
	printf("enter sum of ten numbers:%d",sum);
}