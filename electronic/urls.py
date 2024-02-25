from django.urls import path, include
from rest_framework.routers import DefaultRouter

from electronic.apps import ElectronicConfig
from electronic.views import SupplierViewSet

app_name = ElectronicConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [

] + router.urls
