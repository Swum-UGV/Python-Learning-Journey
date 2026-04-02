list1=[1,2,3,4,5]
list2=[6,7,8,9]
def overlap(list1,list2):
    c=len(list1)
    d=len(list2)
    for i in range(0,c):
      for j in range(0,d):
        if list1==list2:
          return
    return 0
if (overlap(list1,list2)):
  print('OVERLAP')
else:
  print('NOT')