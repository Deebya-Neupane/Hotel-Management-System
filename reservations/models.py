from django.db import models
from base.models import User

# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=200)
    amenities = models.CharField(max_length=200)
    
class Room(models.Model):
    room_number = models.IntegerField()
    description = models.TextField()
    type = models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=200)
    price = models.FloatField()
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    is_active = models.BooleanField(default=True)

class Invoice(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
