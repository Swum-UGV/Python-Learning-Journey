print('Press 1 for adding')
print('Press 2 for substract')
print('Press 3 for multiply')
print('Press 4 for divide')
userinput=int(input('Please choose one from above:'))
if userinput <1 or userinput>4:
    print('You must enter from 1 to 4:')
else:
 firstnumber=int(input('Enter the first number:'))
 secondnumber=int(input('Enter the second number:'))
 if userinput==1:
    result=firstnumber+secondnumber
 elif userinput==2:
    result=firstnumber-secondnumber
 elif userinput==3:
    result=firstnumber*secondnumber
 elif userinput==4:
    result=firstnumber/secondnumber
 print('The result is:',result)

