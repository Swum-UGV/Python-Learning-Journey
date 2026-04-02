def bShop(name,quality,unit,tlist=None):
    if not tlist:
        tlist=[]
    tlist.append('{0} {1} {2}'.format(name,quality,unit))
    return tlist
store1=bShop('java',1,'book')
bShop('python',2,'book',store1)
store2=bShop('c++',3,'book')
bShop('js',4,'book',store2)
bShop('assembly',5,'book',store2)
bShop('golang',10,'book',store1)
print(store1)
print(store2)