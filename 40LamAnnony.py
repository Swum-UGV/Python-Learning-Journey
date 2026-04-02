#anonymous function
#lambda expression or anonymous
x=lambda x,*args,y,**kwargs:(x,args,y,kwargs)
print(x(10,'a',2,'b',y=10,i=9,j=10,k=11))