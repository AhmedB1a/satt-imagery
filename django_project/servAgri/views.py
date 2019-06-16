from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Farmer, Donnecap, Parceagri, Polygon, ROIPolygone
from .newnorm import *
from .serializers import FarmerSerializer, DonnecapSerializer, ParceagriSerializer, PolygonSerializer, ROIPolygoneSerializer
from django.http import JsonResponse
from .callPython import *
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class FarmerView(viewsets.ModelViewSet):
	queryset = Farmer.objects.all()
	serializer_class = FarmerSerializer


class ParceagriView(viewsets.ModelViewSet):
	queryset = Parceagri.objects.all()
	serializer_class = ParceagriSerializer


class DonnecapView(viewsets.ModelViewSet):
	queryset = Donnecap.objects.all()
	serializer_class = DonnecapSerializer


class PolygonView(viewsets.ModelViewSet):
	queryset = Polygon.objects.all()
	serializer_class =  PolygonSerializer

class ROIPolygoneView(viewsets.ModelViewSet):
   queryset = ROIPolygone.objects.all()
   serializer_class = ROIPolygoneSerializer



page = """
<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		{% block title %} <title>Image data</title> {% endblock %}
	</head>

	<body>

		<header>
			<p> the canvas</p>
			<div class="indeces">
				<span class="pl-3"><input type="checkbox" class="input-chexkbox" id="sr" onclick="get_index(this)" />sr
				</span>
				<span class="pl-3"><input type="checkbox" class="input-chexkbox" id="ndvi" onclick="get_index(this)" />ndvi
				</span>
				<span class="pl-3"><input type="checkbox" class="input-chexkbox" id="tvi" onclick="get_index(this)" />tvi
				</span>
				<span class="pl-3"><input type="checkbox" class="input-chexkbox" id="ttvi" onclick="get_index(this)" />ttvi
				</span>
				<span class="pl-3"><input type="checkbox" class="input-chexkbox" id="rvi" onclick="get_index(this)" />rvi
				</span>
			</div>
			<div id="show"></div>
			<canvas id="myCanvas" width="1090" height="600"></canvas>
		</header>

		<script>
			
			function get_index(inputObj) {
				var indexes = "";
				var chkbox = document.getElementsByClassName("input-chexkbox");
				//for(var i = 0; i < chkbox.length; i++){
				if (inputObj.checked == true) {
					indexes += inputObj.id + " ";
					/*$.ajax({
						type:"POST",
						url: "~/python.py",
						data: {parm: text}
					}).done(function( o ){
						//
					});*/
					var xhr = new XMLHttpRequest();
					xhr.open("GET", "callPython.py", true);
					xhr.responseType = "JSON";
					xhr.onload = function (e) {
						var arrOfStrings = JSON.stringify(xhr.response);

					}
					xhr.send();
					alert("ok");
				}
				//}
				alert(indexes);
			}

		</script>

	</body>

</html>
"""

class CallFunction(View):
	def post(self, request):
		x = CallPython()
		index = request.POST.get("index")
		return x.get_index(index)

def all_points(request, id):
	c = Calculation()
	#x = c.pol_points(id)
	x = []
	x = c.end_points(id)
	# jsonR = JsonResponse( context, safe=False)
	context = {
		# 'jsowR': jsonR,
		'id': id,
		'count': len(x),
		'points': x,
	}
	return  JsonResponse( context, safe=False) # render(request, page, context) # 

def getIndexes(request, index):
	i = CallPython()
	j = []

	j = i.get_index(indexid=index)
	context = {
		'indexes': j
	}
	return # JsonResponse( context, safe=False) #  j # render(request, page, context) # 

def getData(request):
	return render(request, 'test2.html', {'title': ' t e s t 2 ',} )
	
# """ from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# import json
# from servAgri.models import Farmer, Parceagri, Donnecap

# def index(request):
	#     response = json.dumps([{}])
	#     return HttpResponse(response, content_type='text/json')

	# def get_farmer(request, framer_name):
	#     if request.method == 'GET':
	#         try:
	#             farmer = Farmer.objects.get(firstName=framer_name)
	#             response = json.dumps([{ 'Farmer first name': farmer.firstName, 'farmer last name': farmer.lastName, 'Email': farmer.email}])
	#         except:
	#             response = json.dumps([{ 'Error': 'No farmer with that name'}])
	#     return HttpResponse(response, content_type='text/json')

	# @csrf_exempt
	# def add_farmer(request):
	#     if request.method == 'POST':
	#         payload = json.loads(request.body)
	#         farmer_fisrt_name = payload['firstName']
	#         farmer_last_name = payload['lastName']
	#         famer_email = payload['email']

	#         farmer = Farmer(firstName=farmer_fisrt_name, lastName=farmer_last_name, email=famer_email)
	#         try:
	#             farmer.save()
	#             response = json.dumps([{ 'Success': 'Car added successfully!'}])
	#         except:
	#             response = json.dumps([{ 'Error': 'Car could not be added!'}])
	# return HttpResponse(response, content_type='text/json') """
