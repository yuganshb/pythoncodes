import cmath
import random
import time

t=time.clock()

#-------------------------------------------------- Ordinary multiply-------------------------------------------
def normal_multiplication(a,b):
	d=[]
	for i in range(0,len(a)):
		d.append(0)
	n=len(a)
	for k in range(0,n):
		for i in range(0,k+1):
			d[k]+=a[i]*b[k-i]
	return d

#--------------------------------------------------------FFT FUNCTION------------------------------------------------------------
def fft(a,w):
  
  if(len(a)==1):
    return a
  else:
    ae=a[::2]
    ao=a[1::2]
    
    fe=fft(ae,w**2)
    fo=fft(ao,w**2)
    m=len(a)
    f=[0 for i in range(m)]
    x=1
    n=m//2
    for j in range(0,n):
      f[j]=(fe[j]+x*fo[j])
      f[j+n]=(fe[j]-x*fo[j])
      x=x*w
    return f



#---------------------------------------------------------MAIN DEFINITION-------------------------------------------------------------

print("enter size of polynomial :- ")
n=int(input())

w1=cmath.exp((1*cmath.pi*1j)/n)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ INPUT ++++++++++++++++++++++++++++++++++++++++++++++++++++
a=[0]*(2*n)
b=[0]*(2*n)
for i in range(0,n):
  a[i]=random.randint(0,10)
  b[i]=random.randint(0,10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ FFT Start ++++++++++++++++++++++++++++++++++++++++++++++++++
a1=fft(a,w1)
b1=fft(b,w1)

c1=[0]*(2*n)
for i in range(0,2*n):
  c1[i]=a1[i]*b1[i]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++ IFFT ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
w2=cmath.exp((-1*cmath.pi*1j)/n)

c = fft(c1,w2)
  
for i in range(len(c)):
  c[i]=c[i]/(2*n)

#+++++++++++++++++++++++++++++++++++++++++++++++++++ Answer Print ++++++++++++++++++++++++++++++++++++++++++++++++

print(a)
print(b)
print(c)
print("\n\n\n")
print(normal_multiplication(a,b))
print(time.clock()-t)
#---------------------------------------------------- END -------------------------------------------------------------------
