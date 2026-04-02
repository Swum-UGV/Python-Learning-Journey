words=[]
while True:
   user=input('enter the words:')
   if user=='':
      break
   words.append(user)
unique_word=[]
for word in words:
   if word not in unique_word:
      unique_word.append(word)
print(unique_word)