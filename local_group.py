 def process_line(self,raw_data,trail_number):
        """ Takes a line of raw gps data and returns latitude,longitude and timestamp """

        line= raw_data.split(',')
        #print line
        latitude, longitude, timestamp = line[0],line[1], line[2].split()[0]
        return latitude,longitude, timestamp,trail_number