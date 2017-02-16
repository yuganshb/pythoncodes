func<-function()
{
  mean<-5;
  x0<-123;
  a<-1597;
  m<-244944;
  y<-x0;
  u<-vector(len=5000);
  exp<-vector(len=5000);
  
  for(i in 1:5000)
  {
    y<-((a*y)%%m);
    if(y<0)
      y<-y+m;
    
    u[i]<-y/m;
    exp[i]<--mean*log(1-u[i]);
  }
  png("exp_R.png");
  hist(exp,breaks=50,col='black',plot=TRUE);
  dev.off();
  
  cat("\nThe mean of values generated is ",mean(exp))
  cat("\nThe maximum is ",max(exp))
  cat("\nThe minimum is ",min(exp),"\n") 
}
