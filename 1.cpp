#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
   int t,i,j,n;
   cin>>t;

   long long a[n],k,arr1[t];
   char arr[n];
   for(i=0;i<t;i++)
   {
       cin>>n;
       cin>>k;
       for(j=0;j<n;j++)
       {
           cin>>a[j];
           if(a[j]%k==0)
           {
             arr[j]='1';
           }
           else{arr[j]='0';}
       }
      arr1[i]=(long long)arr;
   }
    for(i=0;i<n;i++)
    {
        cout<<arr1[i]<<endl;
    }
}