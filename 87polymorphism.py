class AgAg:
    def human(self):
        print('AgAg is a programmeer')
        print('AgAg is always coding')
class MgMg:
    def human(self):
        print('MgMg is a hacker')
        print('MgMg is always learning')
class KoKo:
    def human(self):
        print('KoKo is a programmer')
        print('KoKo is always coding')
class People:
    def fun(self,obj): 
        obj.human()
agag=AgAg()
mgmg=MgMg()
koko=KoKo()
people=People()
mylist=[agag,mgmg,koko]
for a in mylist:
    people.fun(a)