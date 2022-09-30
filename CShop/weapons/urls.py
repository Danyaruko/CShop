from django.urls import include, path
from rest_framework import routers
from weapons import views


router = routers.DefaultRouter()
router.register(r'weapons', views.WeaponViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
