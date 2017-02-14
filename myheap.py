def maxheapify(a,i,n):
  l=2*i+1
  r=2*i+2
  lar=i
  
  if(l<n and a[lar]<a[l]):
    lar=l
  if(r<n and a[lar]<a[r]):
    lar=r
    
  if(lar!=i):
    a[i],a[lar]=a[lar],a[i]
    maxheapify(a,lar,n)

def build_heap(a,n):
  for i in range((n-1)//2,-1,-1):
    maxheapify(a,i,n)
