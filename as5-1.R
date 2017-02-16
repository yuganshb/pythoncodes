f<-function(x)
{
   return (exp(-1*(abs(x)-1)*(abs(x)-1)/2));
}

func<-function(n)
{	
	u<-vector(length=n);
	lap<-vector(length=n);
	fulln<-vector(length=n);
	
	u<-runif(n,0,1);
        
        for(i in 1:n) 
	 fulln[i]<-0;
	
	for(j in 1:n)
	 {
	   if(u[j]<0.5)
            lap[j]=log(2*u);
           if(u[j]>=0.5)
            lap[j]=-1*log(2*(1-u));
         }
         
         c=sqrt(2*exp(1)/pi);
         for(i in 1:n)
          {
            u1<-runif(1,0,1);
            if(u1<=f(lap[i]))
              fulln[i]=u1;
          }
         
        png("fulln.png");
	hist(fulln, breaks=100, col="blue", plot=TRUE);
	dev.off();
	cat("Mean ",mean(fulln));
        cat("Var ",var(fulln));
}
func(10000);
