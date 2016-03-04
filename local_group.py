import os
import sys
from lib import *



trailpoint=[]



    #def read_data(file_name):
        """ reads the file named file_name and stores it in data_lines """

        input_file= open(file_name,'r')
        temp= input_file.readlines()[1:]
        #print temp

        time_stamp = temp[0].split()[0].split(',')
        time = [int(i) for i in time_stamp[-1].split(':')]
        hr,minu,sec=time[0],time[1],time[2]
	for i in temp:
            each_line = i
            line = each_line.split(',')
            time_stamp = line[2].split()[0]
            time = [int(j) for j in time_stamp.split(':')]
            trailpoint.append(each_line)
            
	input_file.close()
        
     """def compare_time(self,time1,time2):
        
        for i in xrange(0,len(time1)):
            if(time1[i] > time2[i] ):
                return 1
            elif(time1[i] < time2[i] ):
                return -1
            else:
                continue
        return 0"""

      def process_line(raw_data):
        """ Takes a line of raw gps data and returns latitude,longitude and timestamp """

        line= raw_data.split(',')
        #print line
        latitude, longitude, timestamp = line[0],line[1], line[2].split()[0]
        return latitude,longitude, timestamp

     def get_zero_speed_data():
        """ 
            stores the duplicate contiguous points in a list. 
            compare each line of gps data with the next one, group them if they are same
            and store them in the list zero_speed_data once a different line of data has been
            found and start a new group.
            the list zero_speed_data contains only the first point of each group and contains
            an additional attribute count to store the number of duplicate contiguous points present (excluding itself).

            output list: latitude,longitude,timestamp,count,local_group_number
                         where count= number of duplicate contiguous points
        
        """
        #print ">",self.data_lines
        count=0
        #get the first point from the raw trail data

        if data_lines == []:
            return

        current_latitude, current_longitude, current_timestamp= process_line(data_lines[0])
        
        for next_line in data_lines[1:]:
            #get the next point
            next_latitude, next_longitude, next_timestamp= process_line(next_line)
            #if current and next points are same, duplicate points found, increment count
            if (current_latitude,current_longitude) == (next_latitude,next_longitude):
                count+=1
            else:
                #if there is at least one additional duplicate point
                if count>0:
                    #add the first point of the group to the zero_speed_list
                    zero_speed_data.append([current_latitude,current_longitude,current_timestamp,count,trail_number])
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
            distance= dist(float(current_point[0]),float(each_point[0]),float(current_point[1]),float(each_point[1]))
            
            if distance > DISTANCE_THRESHOLD:
                #create a new group
                local_group_no+=1
            #assign each point to local_group_no
            #point to note: local_group_no doesn't change if the distance between two points is <= distance_threshold.
            
            each_point= each_point + [local_group_no] #append the local_group_no (changed/unchanged) to the next point
            local_group_data.append(each_point)
            current_point= each_point #assign each_point to the current_point


        def get_local_group_leaders(self):
        
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
        
        self.local_group_data.append([-12])

        group=[] #stores a group of points temporarily
        group_number=1
        for each_point in self.local_group_data:
            #check the local group number for each point, if it is equal to  group_number append it to group
            if each_point[-1] == group_number:
                group.append(each_point)
            else:
                #get the group leader of the current group
                group_leader= get_group_leader(group)
                #and append it to local_group_leader[]
                self.local_group_leader.append(group_leader)
                group_number+=1 #create a new group
                group=[] #reset group[]
                group.append(each_point) #add the current point to the new group
        self.local_group_data.pop() # removing the dummy variable
