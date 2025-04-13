from django.db import models
from django.utils.translation import gettext as _


class Plant(models.Model):
   Soil_Moisture= models.IntegerField(_("Soil Moisture"))
   Temperature= models.IntegerField(_("Temperature"))
   Soil_Humidity= models.IntegerField(_("Soil Humidity"))
   Air_temperature= models.FloatField(_("Air temperature (C)"))
   Air_humidity= models.FloatField(_("Air humidity (%)")) 
   Pressure= models.FloatField(_("Pressure (KPa)"))
   ph= models.FloatField(_("ph"))
   Status= models.IntegerField(_("Status"))
   rainfall= models.FloatField(_("rainfall"))
   

# Create your models here.
