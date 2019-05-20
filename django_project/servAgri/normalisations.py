from .models import * 



# L = / longitude de P1 - longitude de P2 /
# H = / 
# Donnecap.objects.get(id)
# 


#class calculation: 
#    def __init__(): 
#        pass 
    

 #   l = l 
#    def callOfTheImageCoor():
        
  #      psg_and_pid_coordinates = Donnecap.objects.all()
  #      pointsOfPolygone = ROIPolygone.objects.all()

#        for i in psg_and_pid_coordinates:
 #           psg_lat = i.psg_lat
 #           psg_lon = i.psg_lon
 #           pid_lat = i.pid_lat
 #           pid_lon = i.pid_lon
        #the a methode to convert a multiple numbers to another format by using map and split 
 #       return psg_lat, psg_lon, pid_lat, pid_lon
        

 #   def dataOfPoints():
 #       roi = ROIPolygone.objects.all()
 #       x = Donnecap.objects.get(id_donnecap = 1)
        #PSG_latitude_x1 = float(x.psg_lat)
        #PSG_longitude_y1 = float(x.psg_lon)
        #PID_latitude_x4 = float(x.pid_lat)
        #PID_longitude_y4 = float(x.pid_lon)

        #rectangle_length_L = abs(PID_latitude_x4 - PSG_latitude_x1)
        #rectangle_width = abs(PSG_longitude_y1 - PID_longitude_y4)
        #return rectangle_length_L, rectangle_width

 #   def calculate():
        
        #rectangle_length_L
        #rectangle_width

    #About the points from 1 to 7 
    # l' = abs( ) 

#psg_lat, psg_lon, pid_lat, pid_lon = calculation.callOfTheImageCoor()
#float(psg_lat)


class Calculation:
    def __init__(self, *args, **kwargs ):
        pass 
    # this function get called by two functions: call_of_the_image_coor_length and call_of_the_image_coor_width
    def calc(self, one = [], two = []):
        f = []
        for i in range(len(one)):
            f.append(abs(one[i] - two[i]))
        return f

    #this two functions caculate the length and the width of the image, 
    # but the result with decimal.Decimal format, so I need to convert them for calculas reason 

    def call_of_the_image_coor_length(self):
        self.psg_lat = []
        self.psg_lon = []
        self.pid_lat = []
        self.pid_lon = []
        n = Donnecap.objects.all()
        for i in n:
            self.psg_lat.append(i.psg_lat)
            self.psg_lon.append(i.psg_lon)
            self.pid_lat.append(i.pid_lat)
            self.pid_lon.append(i.pid_lat)
        return self.calc(one = self.psg_lat, two = self.pid_lat)
    
    def call_of_the_image_coor_width(self):
        self.psg_lon = []
        self.pid_lon = []
        n = Donnecap.objects.all()
        for i in n:
            self.psg_lon.append(i.psg_lon)
            self.pid_lon.append(i.pid_lon)
        return self.calc(one = self.psg_lon, two = self.pid_lon)

    def call_of_polygon_points(self):
            roi = ROIPolygone.objects.all()
            self.pid_lat_point_x = []
            self.pid_lon_point_y = []
            for i in roi: 
                pass

    def norm_calc():
        roi = ROIPolygone.objects.all()
        x= []
        y = [] 
        for i in roi:
            x.append(i.lat)
            y.append(i.lat)
        return x, y 
    # for lontitude points
    def pol_point_lon(self):
        c = ROIPolygone.objects.values_list( 'lat', 'lon')
        self.axis = []
        for i in c:
            self.axis.append(i[1])
        return self.point_lon_to_float(data = self.axis)

    def point_lon_to_float(self, data):
        loubya = [float(i) for i in data]
        return loubya

    #-----------------------------------------------
    # for latitude points
    
    def pol_point_lat(self):
        c = ROIPolygone.objects.values_list( 'lat', 'lon')
        self.axis = []
        for i in c:
            self.axis.append(i[0])
        return self.point_lon_to_float(data = self.axis)
    # Contains the points that we need already on the calculas
    def new_points(self):
        self.lat1, self.lat2, self.lat3, self.lat4, self.lat5, self.lat6 = self.pol_point_lat()
        self.lon1, self.lon2, self.lon3, self.lon4, self.lon5, self.lon6 = self.pol_point_lon()
        self.length = self.call_of_the_image_coor_length()
        self.width = self.call_of_the_image_coor_width()
        self.psg_lat = 35.596080
        self.psg_lon = -0.79828

        self.l1 = abs(self.lat1 - self.psg_lat)
        self.h1 = abs(self.lon1 - self.psg_lon)
        self.l2 = abs(self.lat2 - self.psg_lat)
        self.h2 = abs(self.lon2 - self.psg_lon)
        
        self.l3 = abs(self.lat3 - self.psg_lat)
        self.h3 = abs(self.lon3 - self.psg_lon)
        self.l4 = abs(self.lat4 - self.psg_lat)
        self.h4 = abs(self.lon4 - self.psg_lon)
        self.l5 = abs(self.lat5 - self.psg_lat)
        self.h5 = abs(self.lon5 - self.psg_lon)
        self.l6 = abs(self.lat6 - self.psg_lat)
        self.h6 = abs(self.lon6 - self.psg_lon)
        return self.l1, self.h1, self.l2, self.h2, self.l3, self.h3, self.l4, self.h4,self.l5, self.h5, self.l6, self.h6
    
    # this function contains all the lenght and width of the points of the polygon 
    def end_points(self): 
        self.l1, self.h1, self.l2, self.h2, self.l3, self.h3, self.l4, self.h4,self.l5, self.h5, self.l6, self.h6 = self.new_points()
        #self.l = self.call_of_the_image_coor_width()
        #self.l = [float(s) for s in self.l]
        #self.h = self.call_of_the_image_coor_length()
        #self.h = [float(s) for s in self.h]
        self.l = self.convert_l()
        self.h = self.convert_h()
        self.result = self.l / self.l
        self.p1 = (self.l1/self.l, self.h1/self.h)
        self.p2 = ( self.l2/self.l , self.h2/self.h )
        self.p3 = ( self.l3/self.l , self.h3/self.h )
        self.p4 = ( self.l4/self.l , self.h4/self.h )
        self.p5 = ( self.l5/self.l , self.h5/self.h )
        self.p6 = ( self.l6/self.l , self.h6/self.h )
        return self.p1, self.p2, self.p3, self.p4 , self.p5, self.p6
    # this will convert the width of the image from decimal.Decimal to an flaot type 
    # for a calculation reason 
    def convert_h(self):
        self.h = self.call_of_the_image_coor_width()
        self.h = [ str(i) for i in self.h]
        self.res = float("".join(self.h))
        return self.res


    #this will convert the lenght of the photo from decimal.Decimal to an float type 
    def convert_l(self):
        self.l = self.call_of_the_image_coor_length()
        self.l = [ str(i) for i in self.l]
        self.l = float("".join(self.l))
        return self.l    











