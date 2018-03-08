from django.db import models

# Create your models here.


class RainData(models.Model):
    longitude = models.DecimalField(decimal_places=2, max_digits=5)
    latitude = models.DecimalField(decimal_places=2, max_digits=5)
    rain_jan = models.DecimalField(decimal_places=2, max_digits=5)
    rain_feb = models.DecimalField(decimal_places=2, max_digits=5)
    rain_mar = models.DecimalField(decimal_places=2, max_digits=5)
    rain_apr = models.DecimalField(decimal_places=2, max_digits=5)
    rain_may = models.DecimalField(decimal_places=2, max_digits=5)
    rain_jun = models.DecimalField(decimal_places=2, max_digits=5)
    rain_jul = models.DecimalField(decimal_places=2, max_digits=5)
    rain_aug = models.DecimalField(decimal_places=2, max_digits=5)
    rain_sep = models.DecimalField(decimal_places=2, max_digits=5)
    rain_oct = models.DecimalField(decimal_places=2, max_digits=5)
    rain_nov = models.DecimalField(decimal_places=2, max_digits=5)
    rain_dec = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        unique_together = ('longitude', 'latitude',)

    def __str__(self):
        return '<Longitude: {}, Latitude: {}>'.format(self.longitude, self.latitude)
    
    def rainWaterCalculation(self, roofArea, roofCoeff):
        result = {}
        result['jan'] = roofArea*self.rain_jan*roofCoeff
        result['feb'] = roofArea*self.rain_feb*roofCoeff
        result['mar'] = roofArea*self.rain_mar*roofCoeff
        result['apr'] = roofArea*self.rain_apr*roofCoeff
        result['may'] = roofArea*self.rain_may*roofCoeff
        result['jun'] = roofArea*self.rain_jun*roofCoeff
        result['jul'] = roofArea*self.rain_jul*roofCoeff
        result['aug'] = roofArea*self.rain_aug*roofCoeff
        result['sep'] = roofArea*self.rain_sep*roofCoeff
        result['oct'] = roofArea*self.rain_oct*roofCoeff
        result['nov'] = roofArea*self.rain_nov*roofCoeff
        result['dec'] = roofArea*self.rain_dec*roofCoeff
        return result
