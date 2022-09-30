from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from weapons.constants import WeaponType, OrderStatus


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=WeaponType.choices())
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='weapons_images', null=True, blank=True)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.deletion.CASCADE)
    weapon = models.ForeignKey(to=Weapon, on_delete=models.deletion.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=100, default=OrderStatus.PENDING, choices=OrderStatus.choices())
