a=int(input('enter three numbers:'))
if a<=99 or a>=999:
    print('worng')
else:
    b=a//100
    c=(a%100)//10
    d=a%10
    digit_sum=b+c+d
    result_a=digit_sum%2==0
slide1=float(input('enter nums:'))
slide2=float(input('enter nums:'))
slide3=float(input('enter nums:'))
is_traingle=slide1+slide2>slide3 and slide1+slide3>slide2 and slide2+slide3>1
is_scalene=slide1!=slide2 and slide1!=slide3 and slide2!=slide3
result_b=is_traingle and is_scalene
print('is it even:',result_a)
print('is traingle and scalene:',result_b)
