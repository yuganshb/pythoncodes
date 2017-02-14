from myheap import maxheapify,build_heap
class prq:
  def __init__(self,a):
    self.heap=a
    self.n=len(a)-1
    build_heap(self.heap,self.n+1)
  
  def maximum(self):
    return self.heap[0]
  
  def remove_maximum(self):
    self.heap[0],self.heap[self.n]=self.heap[self.n],self.heap[0]
    build_heap(self.heap,self.n)
    self.n=self.n-1
    
    
  def increase_key(self,i,x):
    self.heap[i]=x
    while(self.heap[i]>self.heap[self.parent(i)] and self.parent(i)>=0):
      self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
      i=self.parent(i)
  
  def insert(self,x):
    self.heap.append(float('-inf'))
    self.n=self.n+1
    self.increase_key(self.n,x) 
     
  
  def printheap(self):
    print(self.heap[:self.n+1]) 
   
  def lenheap(self):
    return self.n
  
  def parent(self,i):
    return (i-1)//2
