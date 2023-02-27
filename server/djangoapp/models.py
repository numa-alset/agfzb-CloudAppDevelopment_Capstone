from django.db import models
from django.utils.timezone import now
from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    car_name = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    def __str__(self):
        return self.car_name + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CarModel_name = models.CharField(max_length=10)
    dealerId = models.IntegerField()
    carmodel = [
        ('Wagon', 'Wagon'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
    ]
    typeModel = models.CharField(max_length=10,choices=carmodel)
    year = models.DateField()
    car = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    def __str__(self):
        return self.CarModel_name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data



