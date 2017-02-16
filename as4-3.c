#include<stdio.h>
#include<math.h>
int check(float z)
{
  int pos,i;
  float a[]={0.0,5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0};
   for(i=0;i<21;i++)
    {
        if(z<=a[i]/100)
        {
           pos=i;
           break;
        }
    }
   return pos;
}

float f(float x)
{
   return (20*x*pow((1-x),3));
}

void main()
{
   int c=3;
   float z,f2[5000],f1[5000],g[5000],mean=0;
   int i=0,j,freq[20]={0};
   long int y,x=123; 
   while(i<5000)
   {
      y=(1597*x)%244944;
      z=(float)((float)y/244944);
      f2[i]=z;
       i++;
      x=y;
   }
   i=0;
   x=34;
   
   while(i<5000)
   {
      y=(1597*x)%244944;
      z=(float)((float)y/244944)*3;
      f1[i]=z;
 
      i++;
      x=y;
   }
   
    
   for(i=0,j=0;i<5000;i++)
   {
   
     if(3*f1[i]<=f(f2[i]))
      {
         g[j]=f2[i];
         j++;
      }
    }
   for(i=0;i<j;i++)
    {
      freq[check(g[i])-1]++;
    }
    for(i=0;i<20;i++)
     printf("%d %.2f %d\n",i,i*0.05,freq[i]);
     
 }
