a=input('enter something:')
vowels='aeiouAEIOU'
count=0
for char in a:
    if char in vowels:
        count+=1
print(count)