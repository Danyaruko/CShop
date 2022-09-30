from rest_framework import viewsets
from weapons.models import Weapon, Order
from weapons.serializers import WeaponSerializer, OrderSerializer


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer