from .quickIndexs import QuickIndex as i
from django.http import HttpResponse, StreamingHttpResponse
import io
from wsgiref.util import FileWrapper
from .histo_calc import get_ix as histo

class CallPython:
	def __init__(self, *args, **kwargs ):
		pass 

	# this function get called by two functions: call_of_the_image_coor_length and call_of_the_image_coor_width

	def get_index(request, indexid):
		#idx = [indexid]
		idx = [indexid]
		#red_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif" 
		#nir_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif"
		red_file = "D:\\careers\\python-my-projects\\issues\\projects\\dstl-satellite-waterways-master\\data\\scaled_size.tif"
		nir_file = "D:\\careers\\python-my-projects\\issues\\projects\\dstl-satellite-waterways-master\\data\\scaled_size.tif"
		green_file = "D:\\careers\\python-my-projects\\issues\\projects\\dstl-satellite-waterways-master\\data\\scaled_size.tif"
		qi = i(idx, red = red_file, nir = nir_file)
		""" 		output = io.BytesIO()
		
		response = StreamingHttpResponse(FileWrapper(\
			open("D:\\careers\\python-my-projects\\issues\\projects\\dstl-satellite-waterways-master\\outp\\ndvi-image.png"\
				, "rb"), 8192), content_type="image/png")  """
		#return 'response'
		#import time
		#time.sleep(20)
		histo(indexid)

		return qi
		
	def ndvi_img(request):
		return HttpResponse("<img src='/ndvi/img'>")

	def post_file(self=None):
		f = "D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\\django_project\\servAgri\\output\\test.txt"
		open(f, 'w')


		""" class CallPython:
			def __init__(self, *args, **kwargs ):
				pass 

			# this function get called by two functions: call_of_the_image_coor_length and call_of_the_image_coor_width

			def get_index(request, indexid):
				#idx = [indexid]
				idx = indexid
				red_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif"
				nir_file = "C:\\Users\\Lenovo\\Desktop\\koko\\20160831_180302_0e26_3B_AnalyticMS.tif"

				qi = i(idx, red = red_file, nir = nir_file)
				output = io.BytesIO()
				
				response = StreamingHttpResponse(FileWrapper(\
					open("D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\\django_project\\servAgri\\output\\ndvi-image.png"\
						, "rb"), 8192), content_type="image/png")
				return response
				
			def ndvi_img(request):
				return HttpResponse("<img src='/ndvi/img'>")

			def post_file(self=None):
				f = "D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\\django_project\\servAgri\\output\\test.txt"
				open(f, 'w')
		"""
