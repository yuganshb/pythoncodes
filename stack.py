class mystack:

  def __init__(self,a):
    self.stack=a
    self.t=len(a)-1
    
  def isempty(self):
    if(self.top()==0):
      return 1
    else :
      return 0
  
  def top(self):
    return self.t
  
  def pop(self):
    self.t=self.t-1
    return self.stack[self.t+1]
    
  
  def push(self,x):
    self.stack[self.t+1]=x
    self.t=self.t+1
  
  def print(self):
    print(self.stack[:self.t+1])

a=mystack([5,2,31,4,6,7])
print(a.isempty())
a.print()
a.pop()
a.print()
a.pop()
a.print()
a.push(24)
a.print()



