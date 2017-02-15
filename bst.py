class node:
  def __init__(self,data=None):  
    self.key=data
    self.l=None
    self.r=None
    self.p=None

class bst:

  def __init__(self):
    self.root=None
    
  def insert(self,r,n):
    if(r.key==None):
      r=n
      return
  
    x=r
    while(x.l is not None or x.r is not None):
      if(x.key>n.key):
        x=x.l
      else:
        x=x.r
    
    if(x.key>n.key):
      x.l=n
    else:
      x.r=n
    
    self.root=r


root=node()
n=node()
a=bst()
a.insert(root,n)
print(a.root.key)
print(a.root.r.key)
    
      
