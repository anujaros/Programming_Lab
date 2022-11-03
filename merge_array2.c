#include<stdio.h>
void main()
{
int a[10],i,n,b[10],m,merge[20],x;
printf("enter the size of array 1:\n");
scanf("%d",&n);

printf("enter the array elements:\n");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("array 1 elements are:");
for(i=0;i<n;i++)
{
printf("%d",a[i]);
}


printf("enter the size of array 2:\n");
scanf("%d",&m);

printf("enter the array elements:\n");
for(i=0;i<m;i++)
{
scanf("%d",&b[i]);
}
printf("array 2 elements are:");
for(i=0;i<m;i++)
{
printf("%d",b[i]);
}

x=n+m

for(i=0;i<n;i++)
merge[i] =a[i];
for(i=0;i<m;i++)
merge[i+n] = b[i];

printf("the merged array:");
for(i=0;i<x;i++)
printf("%d",merge[i]);

}

