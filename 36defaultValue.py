from datetime import datetime
def myFun(msg,*,dt=None):
    if not dt:
        dt=datetime.utcnow()
        print('{0}:{1}'.format(dt,msg))
myFun('text message5')