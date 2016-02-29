from math import *
from geopy.distance import great_circle

def dist(lat1,long1,lat2,long2):
    a = (lat1,long1)
    b = (lat2,long2)
    print(great_circle(a,b).meters)
print dist(1,0,1,1)

