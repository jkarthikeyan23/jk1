#include<iostream.h>
using namespace std;
struct elecount
{
int e;
int c;
};
void morethanNdk(int arr[],int n,int k)
{
if(k<2)
return;
struct elecount temp[k-1];
for(int i=0;i<k-1;i++)
temp[i].c=0;
for (int i=0;i<n;i++)
{
int j;
/* If arr[i] is already present in 
the element count array,then increment its count */
for(j=0;j<k-1;j++)
{
if (temp[j].e==arr[i])
{
temp[j].c+=1;
break;
}
}
if(j==k-l)
{
int l;
for(l=0;l<k-1;l++)
{
if(temp[l].c==0)
{
temp[l].e=arr[i];
temp[l].c=1;
break;
}
}
if(l==k-1)
for(l=0;l<k;l++)
temp[l].c-=1;
}
}
for(int i=0;i<k-1;i++)
{
int ac=0;//actual count
for(int i=0; j<n; j++)
if(arr[j]==temp[i].e)
ac++;
if(ac>n/k)
count<<"number:"<<temp[i].e
<<"count:"<<ac<<endl;
}
}
int main()
{
count<<"Firat test\n";
int arr1[]={4,5,6,7,8,4,4};
int size=sizeof(arr1)/sizeod(arr1[0]);
int k=3;
more thanNdk(arr1,size,k);
count<<"\nSecond test \n";
int arr2[]={4,2,2,7};
size=sizeof(arr2)/sizeof(arr2[0]);
k=3;
more thanNdk(arr2,size,k);
cout<<"\nThird test  \n";
int arr3[]={2,7,2};
size=sizeof(arr3)/sizeof(arr3[0]);
k=2;
more thanNdk(arr3,size,k);
cout<<"\nFourth test\n";
int arr4[]={2,3,3,2};
size=sizeof(arr4)/sizeof(arr4[0]);
k=3;
morethanNdk(arr4,size,k);
return 0;
}
