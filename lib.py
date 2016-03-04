from math import *
import datetime
import time
from geopy.distance import great_circle

def dist(lat1,long1,lat2,long2):
    a = (lat1,long1)
    b = (lat2,long2)
    print(great_circle(a,b).meters)
print dist(1,0,1,1)
<<<<<<< HEAD
def time_compare(hr,minu,sec,hr1,minu1,sec1):
    t1=datetme.time(hr,minu,sec)
    t2=datetime.time(hr1,minu1,sec1)
    if t1>t2:
        return 1
    elif t1<t2:
        return -1
    else:
        return 0
=======
>>>>>>> fb1fe9a61172b38965df6d38b0cd0121d976e86f

