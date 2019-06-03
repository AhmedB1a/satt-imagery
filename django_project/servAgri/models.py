from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum
#import DictionaryField


# Create your models here.


class Farmer(models.Model):
    #id_farmer = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    email = models.EmailField(
        verbose_name='email address', max_length=20, unique=True)

    def __str__(self):
        return self.firstName


class Parceagri(models.Model):
    id_parcelle = models.AutoField(max_length=15, primary_key=True)  # max length
    id_farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    pointDescription = models.TextField(
        
    )
    
    #locati
    def __str__(self):
        return str(self.id_parcelle)


class Donnecap(models.Model):

    id_donnecap = models.AutoField(max_length=15, primary_key=True)
    #id_farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    #id_parcelle = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    id_parcelle = models.ForeignKey(
        Parceagri, on_delete=models.CASCADE, related_name='id_parc')
    # data_type = models.CharField(max_length=10)  # To see (Image/value).

    # """     class Item_type(Enum):
    #    image = "Image"
    #    val = "Value"
    # data_type = models.CharField(
    #    max_length=10,
    #   choices=Item_type, default= Item_type.image
    # ) """
    data_type = models.CharField(default=0, max_length=10)

    #image_blb = models.imageField(blank=true,null=true, upload_to="cover/%Y/%M/%D ")
    image = models.FileField(null=True, blank=True)
    psg_lat = models.DecimalField(default=0, decimal_places=15, max_digits=20)
    psg_lon = models.DecimalField(default=0, decimal_places=15, max_digits=20)
    pid_lat = models.DecimalField(default=0, decimal_places=15, max_digits=20)
    pid_lon = models.DecimalField(default=0, decimal_places=15, max_digits=20)

    image_spectrum = models.IntegerField(default=0,
                                         validators=[
                                             MaxValueValidator(100),
                                             MinValueValidator(1)
                                         ]
                                         )  # limited_integer_field


class Polygon(models.Model):
    name= models.CharField(max_length=13, null=True)
    def __str__(self):
        return self.name


class ROIPolygone(models.Model):
    id_polygon = models.ForeignKey(
        Polygon, on_delete=models.CASCADE, null=True, related_name='id_pol')
    point_number = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])
    lat = models.DecimalField(_('Latitude'), max_digits=17, decimal_places=10)
    lon = models.DecimalField(_('Lontitude'), max_digits=17, decimal_places=10)

# see the data of lat and lon on the parceagri model to delete.
