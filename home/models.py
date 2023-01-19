from django.db import models

# Create your models here.
class cartype(models.Model):
    c_type=models.CharField(max_length=100)
    c_description=models.TextField()

    def __str__(self):
        return self.c_type

class Cars(models.Model):
    car_name=models.CharField(max_length=250)
    car_ty=models.ForeignKey(cartype, on_delete=models.CASCADE)
    car_img=models.ImageField( upload_to='cars')

    def __str__(self):
        return self.car_name

class Booking(models.Model):
    p_name=models.CharField(max_length=250)
    p_phone=models.CharField(max_length=50)
    p_email=models.EmailField( )
    car=models.ForeignKey(Cars,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)