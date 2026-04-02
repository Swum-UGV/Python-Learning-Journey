list1=[1,2,3,3,45,5]
list2=[12,32,42,4,3]
results=list(map(lambda x,y:x+y,list1,list2))
print(results)
for i in results:
    print(i)
for x in results:
    print(x)