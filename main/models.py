from django.db import models

# Create your models here.


class RainData(models.Model):
    longitude = models.DecimalField
    latitude = models.DecimalField
    rain_jan = models.DecimalField
    rain_feb = models.DecimalField
    rain_mar = models.DecimalField
    rain_apr = models.DecimalField
    rain_may = models.DecimalField
    rain_jun = models.DecimalField
    rain_jul = models.DecimalField
    rain_aug = models.DecimalField
    rain_sep = models.DecimalField
    rain_oct = models.DecimalField
    rain_nov = models.DecimalField
    rain_dec = models.DecimalField

    class Meta:
        unique_together = ('longitude', 'latitude',)

    def __str__(self):
        return '<Longitude: {}, Latitude: {}>'.format(self.longitude, self.latitude)