from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50) #campo tipo texto 
    country = models.CharField(max_length=50) #campo tipo texto 
    def __str__(self):
            return self.name
class Monument(models.Model):
    name = models.CharField(max_length=50) #campo tipo text
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    #location es una ForeingKey de city.
    #on_delete=models.CASCADE, en el caso de que se borre el padre se tien que borrar el monumento
    def __str__(self):
            return self.name