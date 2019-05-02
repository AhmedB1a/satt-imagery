from django.contrib import admin
from .models import Farmer, Parceagri, Donnecap, Polygon, ROIPolygone

# Register your models here.
#admin.site.register(Farmer, Parceagri, Donnecap )
admin.site.register(Farmer)
admin.site.register(Parceagri)
admin.site.register(Donnecap)
admin.site.register(Polygon)
admin.site.register(ROIPolygone)
