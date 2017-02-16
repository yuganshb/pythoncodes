Rejection<-function()
{
	x<-vector(length=5000)
	x1<-1000001
	x2<-1000005
	i<-0;
	a<-16807
	b<-0
	m<-2^31-1
	while (i<=5000)
	{
		y<-x1/m;
		x1<-(a*x1+b)%%(m);
		u<-x2/m;
		x2<-((a*x2)+b)%%(m);
		if (u<=((20*y*((1-y)^3)*64)/(27*5))) 
		{
			x[i]<-y;
			i<-i+1;
		}
	}
	
	png("rejection.png");
	hist(x, breaks=50, col="blue", plot=TRUE);
	dev.off();
}
