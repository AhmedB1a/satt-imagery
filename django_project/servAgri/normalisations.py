from .models import * 

class calculation: 
    def __init__(): 
        pass 
    

    l = l 
    def callOfTheImageCoor():
        
        psg_and_pid_coordinates = Donnecap.objects.all()
        pointsOfPolygone = ROIPolygone.objects.all()

        for i in psg_and_pid_coordinates:
            psg_lat = i.psg_lat
            psg_lon = i.psg_lon
            pid_lat = i.pid_lat
            pid_lon = i.pid_lon
        #the a methode to convert a multiple numbers to another format by using map and split 
        return psg_lat, psg_lon, pid_lat, pid_lon
        

    def dataOfPoints():
        roi = ROIPolygone.objects.all()
        x = Donnecap.objects.get(id_donnecap = 1)
        PSG_latitude_x1 = float(x.psg_lat)
        PSG_longitude_y1 = float(x.psg_lon)
        PID_latitude_x4 = float(x.pid_lat)
        PID_longitude_y4 = float(x.pid_lon)

        rectangle_length_L = abs(PID_latitude_x4 - PSG_latitude_x1)
        rectangle_width = abs(PSG_longitude_y1 - PID_longitude_y4)
        return rectangle_length_L, rectangle_width

    #About the points from 1 to 7 
    # l' = abs( ) 

psg_lat, psg_lon, pid_lat, pid_lon = calculation.callOfTheImageCoor()








# L = / longitude de P1 - longitude de P2 /
# H = / 
# Donnecap.objects.get(id)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# /