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
            u1<-runif(1,0,c*(exp(-abs(lap[i]))/2));
            if(u1<=(exp((-lap[i]^2)/2)/sqrt(2*pi)))
              fulln[i]=u1;
          }
         
        png("fulln.png");
	hist(fulln, breaks=10, col="blue", plot=TRUE);
	dev.off();
	cat("yes");
}
func(10000);
