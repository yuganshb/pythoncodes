#include<stdio.h>
#include<math.h>
#include<malloc.h>
int check(float z)
{
  int pos,i;
  float a[]={0.0,5.0,10.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0};
   for(i=0;i<21;i++)
    {
        if(z<=a[i]/2.5)
        {
           pos=i;
           break;
        }
    }
   return pos;
} 

void main()
{
  
  float z,f[5000],mean=0;
  int i=0,freq[20]={0};
  long int y,x=123; 
  while(i<5000)
   {
      y=(1597*x)%244944;
      z=(float)((float)y/244944);
      f[i]=z;
      i++;
      x=y;
   }   
     
  for(i=0;i<5000;i++)
   {
      f[i]=-5*log(1-f[i]);
      mean=mean+f[i];
   }
   
   for(i=0;i<5000;i++)
   {
      freq[check(f[i])-1]++;
   }  
   
   mean=mean/5000;
     
   float max=f[0],min=f[0];
   
   for(i=0;i<5000;i++)
   {  
      if(max<f[i])
        max=f[i];
      if(min>f[i])
        min=f[i];
       
      printf("%f\n",f[i]);
   }
   for(i=0;i<20;i++)
    printf("%d %d\n",i,freq[i]);
  
    printf("\n MEAN IS %f \n MAX IS %f \n MIN IS %f\n",mean,max,min);
}
