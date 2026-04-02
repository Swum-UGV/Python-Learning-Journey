alphabet=['a','b','c','d','e','f','i','o','u','j','k']
def VowelFilter(alphabet):
    vowel = ['a','e','i','o','u']
    if (alphabet in vowel):
        return True
    else:
        return False
FilterVowel=filter(VowelFilter, alphabet)
print(FilterVowel)
for i in FilterVowel:
    print(i)