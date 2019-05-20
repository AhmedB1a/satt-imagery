from .models import * 
import json

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

	def get_image_size(self, w, h):
		self.width = w
		self.height = h

	def call_of_the_image_coor_length(self):
		self.psg_lat = []
		self.pid_lat = []
		n = Donnecap.objects.all()
		for i in n:
			self.psg_lat.append(i.psg_lat)
			self.pid_lat.append(i.pid_lat)
		return self.calc(one = self.psg_lat, two = self.pid_lat)
	
	def call_of_the_image_coor_width(self):
		self.psg_lon = []
		self.pid_lon = []
		n = Donnecap.objects.all()
		for i in n:
			self.psg_lon.append(i.psg_lon)
			self.pid_lon.append(i.pid_lon)
		return self.calc(one = self.psg_lon, two = self.pid_lon)

	def point_lon_to_float(self, data):
		loubya = [float(i) for i in data]
		return loubya

	# for lontitude points
	def pol_points(self, id):
		# c = ROIPolygone.objects.values_list( 'lat', 'lon', 'id_polygon')
		c = []
		# t = {}
		i = 0

		data = json.loads(open('servAgri\\polygons.json', 'r').read())
		
		for fet in data['features'][id]['geometry']['coordinates'][0]:
			new_p = {'lat': fet[0], 'lon': fet[1], 'id_polygon': id}
			c.append(new_p)


		# for key, values in data['features'][3].items():
			#for n in feature['geometry']['coordinates']:
				#print(n)
			# x=c.append(key)
			# print(x)
				
		# data['features'][1-len()]['geometry']['coordinates'][0][1-len()]
		# myvar['features'][2]['geometry']['coordinates'][0]
		axis_lon = []
		axis_lat = []
		for i in c:
			if i['id_polygon'] == id:
				axis_lat.append(i['lat'])
				axis_lon.append(i['lon'])

		axis_lon = point_lon_to_float(self, data=axis_lon)
		axis_lat = point_lon_to_float(self, data=axis_lat)

		return axis_lat, axis_lon # self.point_lon_to_float(self, data=axis_lat), point_lon_to_float(self, data=axis_lon)

	#-----------------------------------------------
	# for latitude points
	
	# Contains the points that we need already on the calculas
	def new_points(self, id):
		self.new_lat, self.new_lon = self.pol_points(id)

		self.new_h = []
		self.new_l = []

		self.psg_lat = 35.596080
		self.psg_lon = -0.79828

		for i in range(len(self.new_lat)):
			self.new_l.append((abs(self.psg_lat - self.new_lat[i])))
			self.new_h.append((abs(self.psg_lon - self.new_lon[i])))

		
		return self.new_h, self.new_l
	
	# this function contains all the lenght and width of the points of the polygon 
	def end_points(self, id): 
		self.end_h = []
		self.end_l = []
		self.end_p = []

		self.end_h, self.end_l = self.new_points(id)

		self.l = self.convert_l()
		self.h = self.convert_h()

		self.result = self.l / self.l

		for i in range(len(self.end_h)):
			self.end_p.append([ self.end_l[i] / self.l, self.end_h[i] / self.h])

		return self.end_p

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
		self.res = float("".join(self.l))
		return self.res











