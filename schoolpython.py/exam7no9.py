words=['heh','clo','gog','pop','egg']
palindrome=[]
for word in words:
    clean=word.lower()
    if clean==clean[::-1]:
        palindrome.append(clean)
print(palindrome)