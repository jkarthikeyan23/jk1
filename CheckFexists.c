#include<stdio.h>
int rec(int i,int j,int k,int n,int array[])
{
 int sum;
 for(i=0;i<j;)
 {
   sum=array[i]+array[j];
   if(sum>k)
   {
    j--;
   }else if(sum<k)
   {
    i++;
   }else if(sum==k)
   {
     printf("Value equal to sum of array[%d]=%d and array[%d]=%d",i,array[i],j,array[j]])
     return 1;//Ture
    }
   }
   return 0;
   }
  int main()
  {
  int n;
  printf("Enter The Value of Number of Arrays=" );
  scanf("%d",&n);
  int array[n],i,j,k,x;
  print("Enter the Number Which you Want to aearch in addition of Two Number=");
  scan("d",&x);
  printf("Enter The Value of Array \n");
  for(i=-0;i<n-1;i++)
  {
   printf("Array[%d]=",i);
   scanf("%d",&array[i]);
  }
 for(i=0;i<=n-1;i++)
 {
  for(j=0;j<=n-1;j++)
  {
  if(array[j]>array[j+1])
  {
   //swapping of two using bitwise operator
   array[j]=array[j]^array[j+1];
   array[j+1]=array[j]^array[j+1];
   array[j]=array[j]^array[j+1];
   }
   }
  }
  k=x;
  j=n-1;
  rec(i,j,k,n,array);
  return 0;
  }
