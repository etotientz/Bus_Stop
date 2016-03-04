<<<<<<< HEAD
import os
import sys
from lib import *



temp=[]
local_group_data=[]
local_group_leader=[]



    

input_file= open(file_name,'r')
temp= input_file.readlines()[1:]
"""for i in temp:
    trailpoint.append(i)
time_stamp = temp[0].split()[0].split(',')
time = [int(i) for i in time_stamp[-1].split(':')]
hr,minu,sec=time[0],time[1],time[2]
for i in temp:
        each_line = i
        line = each_line.split(',')
        time_stamp = line[2].split()[0]
        time = [int(j) for j in time_stamp.split(':')]
        trailpoint.append(each_line)"""
        
     
def process_line(raw_data):
        """ Takes a line of raw gps data and returns latitude,longitude and timestamp """

     line= raw_data.split(',')
     latitude, longitude, timestamp = line[0],line[1], line[2].split()[0]
     return latitude,longitude, timestamp

def get_zero_speed_data():
        
        count=0
        current_latitude, current_longitude, current_timestamp= process_line(temp[0])
        for next_line in temp[1:]:
            next_latitude, next_longitude, next_timestamp= process_line(next_line)
            #if current and next points are same, duplicate points found, increment count
            if (current_latitude,current_longitude) == (next_latitude,next_longitude):
                count+=1
            else:
                #if there is at least one additional duplicate point
                if count>0:
                    #add the first point of the group to the zero_speed_list
                    zero_speed_data.append([current_latitude,current_longitude,current_timestamp,count])
                    count=0 #reset count so as to mark the beginning of a new group
                current_latitude, current_longitude, current_timestamp = next_latitude, next_longitude, next_timestamp
                #assign the next point to be the current point, ie, it is probably the first point of a next zero-speed group



        def get_local_groups(DISTANCE_THRESHOLD):
        """
        assign local group number to each point
        """
        #assign first point of zero_speed_data to be in local group 1
        local_group_no=1
        
        if zero_speed_data == []:
            return
        
        current_point = zero_speed_data[0]+[local_group_no]
        local_group_data.append(current_point)
        
        #for each point in the zero_speed_data list
        for each_point in zero_speed_data[1:]:
            #get distance between the current_point and each_point
            distance= dist(float(current_point[0]),float(current_point[1]),float(each_point[0]),,float(each_point[1]))
            
            if distance > DISTANCE_THRESHOLD:
                #create a new group
                local_group_no+=1
            #assign each point to local_group_no
            #point to note: local_group_no doesn't change if the distance between two points is <= distance_threshold.
            
            each_point= each_point + [local_group_no] #append the local_group_no (changed/unchanged) to the next point
            local_group_data.append(each_point)
            current_point= each_point #assign each_point to the current_point


        def get_local_group_leaders():
        
        """ get all of the local group leader points for all groups in a trail
            we store the group leader points for a trail in local_group_leader[]
        """

        #group the points based on local group_number and store the local group leader of each group


        #attach a dummy variable to the end of local_group_data
        #we'll remove it after operation
        #significance: to append the new group formed after the operation on last element of the list
        #since we add a new group only when we find a change in the local_group_number between consecutive
        #elements, we need to make sure that we have a dummy variable to check the last element of the list with.
        #and form the last group
        
        local_group_data.append([-12])

        group=[] #stores a group of points temporarily
        group_number=1
        for each_point in local_group_data:
            #check the local group number for each point, if it is equal to  group_number append it to group
            if each_point[-1] == group_number:
                group.append(each_point)
            else:
                #get the group leader of the current group
                group_leader= get_group_leader(group)
                #and append it to local_group_leader[]
                local_group_leader.append(group_leader)
                group_number+=1 #create a new group
                group=[] #reset group[]
                group.append(each_point) #add the current point to the new group
            local_group_data.pop() # removing the dummy variable

        def get_group_leader(group):
        """ returns the group_leader point for a particular group of points"""
       
        if group == []:
            return
        wait_per_distance= [] #contains the summation of wait_time/distance from one point to all other point, for every point in the group
        total_wait_time=0  #would contain the total wait time of the group, we sum up the 'count' field of all the points
        for each_point in group:
            wait_time= int(each_point[3])  #each_point= [latitude,longitude,timestamp,count,local_group_number]
            temp=0   #temp would contain wait_time* (1/d1 + 1/d2 + 1/d3 + .....) where d1,d2,d3...dn are distances from one point to all other points
            for other_point in group:
                #get distance from each_point to other_point, d1,d2,d3.... etc
                distance= get_spherical_distance(float(each_point[0]),float(other_point[0]),float(each_point[1]),float(other_point[1]))
                temp+= 1/(distance+1)  # here, temp= (1/d1 + 1/d2 + 1/d3 + .....)
            temp= wait_time*temp        #now, temp= wait_time* (1/d1 + 1/d2 + 1/d3 + ....)
            wait_per_distance.append(temp)  #append temp to the list
            total_wait_time+=wait_time 
        
        max_index=0

        max_wait_per_distance= max(wait_per_distance) #get the maximum value from the list
 
        #get the index of the point having maximum wait_per_distance
        for index in xrange(0,len(wait_per_distance)):
           if max_wait_per_distance == wait_per_distance[index]:
               max_index= index
               break

        group[max_index][3]= total_wait_time  #replace 'count' field with total_wait_time.

        return group[max_index]  #return the group leader point
=======
 def process_line(self,raw_data,trail_number):
        """ Takes a line of raw gps data and returns latitude,longitude and timestamp """

        line= raw_data.split(',')
        #print line
        latitude, longitude, timestamp = line[0],line[1], line[2].split()[0]
        return latitude,longitude, timestamp,trail_number
>>>>>>> fb1fe9a61172b38965df6d38b0cd0121d976e86f
