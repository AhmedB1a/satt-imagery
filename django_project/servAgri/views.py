from django.shortcuts import render
from rest_framework import viewsets
from .models import Farmer, Donnecap, Parceagri, Polygon, ROIPolygone
from .serializers import FarmerSerializer, DonnecapSerializer, ParceagriSerializer, PolygonSerializer, ROIPolygoneSerializer

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
