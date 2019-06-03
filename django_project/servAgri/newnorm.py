from .models import * # we have one this for importing the models. 
import json
import ast

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

	def call_of_the_image_coors(self):
		self.psg_lat = []
		self.pid_lat = []
		
		self.psg_lon = []
		self.pid_lon = []
		
		n = Donnecap.objects.all()
		for i in n:
			self.psg_lon.append(i.psg_lon)
			self.pid_lon.append(i.pid_lon)
		
			self.psg_lat.append(i.psg_lat)
			self.pid_lat.append(i.pid_lat)
		
		return self.calc(one = self.psg_lat, two = self.pid_lat), self.calc(one = self.psg_lon, two = self.pid_lon)
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
	def pol_points1(self, id): # this is old pol points will not used until finsh from new method
	#def pol_points(self, myPoints):
		# c = ROIPolygone.objects.values_list( 'lat', 'lon', 'id_polygon')
		c = []
		# t = {}
		i = 0
		
		"""
			data = Parceagri.objects.filter(id_farmer = 1 ).values('pointDescription', 'id_farmer__firstName', 'id_farmer__lastName', 'id_farmer__email')
			data = data[0]['pointDescription']
			import ast 
			data = ast.literal_eval(data)
			data = data['geometry']['coordinates'][0]
		"""

		"""
		def FarmerAndFarms(id):
			ff = Farmer.objects.all()
			getFarmer = ff[(id - 1)]
			mm = Parceagri.objects.filter(id_farmer=id).values('pointDescription', 'id_farmer__firstName')
			mm = mm[0]['pointDescription']
			mm = ast.literal_eval(mm)
			mm['geometry']['coordinates'][0]
			return mm, id, ff[(id - 1)]
      	"""

		"""
			data = Parceagri.objects.values_list()
			data = Parceagri.objects.values_list('id_farmer', 'pointDescription')
			data = data[0][1]
			data = ast.literal_eval(data)
			data = json.loads(open('servAgri\\polygons.json', 'r').read())
		"""
		
		#for fet in data['features'][id]['geometry']['coordinates'][0]:
		getFarmers = Farmer.objects.all()
		farmerName = getFarmers[(id - 1)]
		getFarms = Parceagri.objects.filter(id_farmer=id).values('pointDescription')
		
		for farm in range(getFarms.count()):
			farmPoints = getFarms[farm]['pointDescription']
			farmPoints = ast.literal_eval(farmPoints)
			new_p = []
			for x, y in farmPoints['geometry']['coordinates'][0]:
				new_p = {'lat': x, 'lon': y}
				c.append(new_p)

		
		# data['features'][1-len()]['geometry']['coordinates'][0][1-len()]
		# myvar['features'][2]['geometry']['coordinates'][0]

		axis_lon = []
		axis_lat = []
		for i in c:
			#if i['id_polygon'] == id:
			axis_lat.append(float(i['lat']))
			axis_lon.append(float(i['lon']))

		# axis_lon = self.point_lon_to_float(data=axis_lon)
		# axis_lat = self.point_lon_to_float(data=axis_lat)

		return axis_lat, axis_lon # self.point_lon_to_float(self, data=axis_lat), point_lon_to_float(self, data=axis_lon)

	
		#mm = Parceagri.objects.filter(id_farmer=id).values('pointDescription', 'id_farmer__firstName')
		#mm = mm[0]['pointDescription']
		#mm = ast.literal_eval(mm)
		#mm['geometry']['coordinates'][0]
		#return mm, id, ff[(id - 1)]

	#-----------------------------------------------
	# for latitude points
	
	# Contains the points that we need already on the calculas
	def pol_points(self, pols): # this is new method of pol points to test some values
		i = 0
		
		axis_lon = []
		axis_lat = []

		for i in pols:
			axis_lat.append(float(i['lat']))
			axis_lon.append(float(i['lon']))

		return axis_lat, axis_lon

	def new_points(self, polPoints): # this is new method for test new points of farmer and his farms
		
		self.new_lon, self.new_lat = self.pol_points(polPoints)

		self.new_h = []
		self.new_l = []

		#self.psg_lat = 35.596080  
		#self.psg_lon = -0.79828

		self.psg_lat = 38.06513049715169
		self.psg_lon = -121.56892418861388

		for i in range(len(self.new_lat)):
			self.new_l.append((abs(self.psg_lat - self.new_lat[i])))
			self.new_h.append((abs(self.psg_lon - self.new_lon[i])))

		
		return self.new_h, self.new_l

	def end_points(self, id): # this is new end points for test farmer and his farms
		
		self.end_lat = []
		self.end_lon = []
		self.end_p = []
		
		self.getFarmers = Farmer.objects.all()
		self.farmerName = self.getFarmers[(id - 1)]
		self.getFarms = Parceagri.objects.filter(id_farmer=id).values('pointDescription')
		
		self.h, self.l = self.convert_size()
		
		if(self.getFarms.count() >= 1):
			
			for farm in range(self.getFarms.count()):
				self.end_pi = []
				farmPoints = self.getFarms[farm]['pointDescription']
				farmPoints = ast.literal_eval(farmPoints)
				new_p1 = []
				new_p2 = []
				for x, y in farmPoints['geometry']['coordinates'][0]:
					xy = []
					xy.append([x, y])
					self.end_pi.append([x, y])
					new_p1.append({'lat': x, 'lon': y})
					
				self.end_lon, self.end_lat  = self.new_points(new_p1)

				for i in range(len(self.end_lat)):
					new_p2.append([ self.end_lon[i] / self.l, self.end_lat[i] / self.h])
			
				self.end_p.append(new_p2)

		else: #if(self.getFarms.count() < 1):
			self.end_p = []
		"""else:
			self.end_pi = []
			farmPoints = self.getFarms[0]['pointDescription']
			farmPoints = ast.literal_eval(farmPoints)
			new_p = []
			for x, y in farmPoints['geometry']['coordinates'][0]:
				new_p = {'lat': x, 'lon': y}
				self.end_pi.append(new_p)
			self.end_lon, self.end_lat  = self.new_points(self.end_pi)

			for i in range(len(self.end_lat)):
				self.end_p.append([ self.end_lon[i] / self.l, self.end_lat[i] / self.h])"""

		
		return self.end_p
	
	"""
	def new_points(self, id):
		self.new_lon, self.new_lat = self.pol_points(id)

		self.new_h = []
		self.new_l = []

		#self.psg_lat = 35.596080  
		#self.psg_lon = -0.79828

		self.psg_lat = 38.06513049715169
		self.psg_lon = -121.56892418861388

		for i in range(len(self.new_lat)):
			self.new_l.append((abs(self.psg_lat - self.new_lat[i])))
			self.new_h.append((abs(self.psg_lon - self.new_lon[i])))

		
		return self.new_h, self.new_l"""
	
	# this function contains all the lenght and width of the points of the polygon 
	
	"""
	def end_points(self, id): 
		self.end_lat = []
		self.end_lon = []
		self.end_p = []

		self.end_lon, self.end_lat  = self.new_points(id)

		#self.l = self.convert_l()
		self.h, self.l = self.convert_size()
		print(self.h, self.l)

		# self.result = self.l / self.l

		for i in range(len(self.end_lat)):
			self.end_p.append([ self.end_lon[i] / self.l, self.end_lat[i] / self.h])

		return self.end_p"""

	# this will convert the width of the image from decimal.Decimal to an flaot type 
	# for a calculation reason 
	def convert_size(self):
		self.h, self.w = self.call_of_the_image_coors()
		self.h = [ str(i) for i in self.h]
		self.w = [ str(i) for i in self.w]

		return float("".join(self.h)), float("".join(self.w))

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











