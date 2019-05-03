from rest_framework import serializers
from .models import Farmer, Parceagri, Donnecap, Polygon, ROIPolygone
class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmer
        fields = ('url', 'firstName', 'lastName', 'email')


class ParceagriSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parceagri
        fields = ('url', 'id_parcelle')


class DonnecapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donnecap
        fields = ('url', 'id_donnecap', 'id_farmer', 'id_parcelle',
         'data_type', 'image', 'psg_lat',
          'psg_lon', 'pid_lat','pid_lon', 'image_spectrum')


class PolygonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Polygon
        fields = ('url', 'id', 'name')


class ROIPolygoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ROIPolygone
        fields = ('url','id_polygon','point_number','lat','lon')





#""" class Item_typeSSerializer(serializers.HyperlinkedModelSerializer):
#   "do nothing" """
