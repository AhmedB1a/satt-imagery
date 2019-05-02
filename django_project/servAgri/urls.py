from django.urls import path, include 
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('farmers', views.FarmerView)
router.register('parcel', views.ParceagriView)
router.register('captedata', views.DonnecapView)
router.register('polygonjhj', views.PolygonView)
router.register('roi', views.ROIPolygoneView)

urlpatterns = [
    path('', include(router.urls))
]
