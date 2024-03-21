from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
router = DefaultRouter()
router.register('locations', LocationMasterViewSet, basename="location")
router.register('categories', CategoryMasterViewSet, basename="category")
router.register('itemmasters', ItemMasterViewSet, basename="itemmaster")
router.register('inventorymasters', InventoryMasterViewSet, basename="inventorymasters")
router.register('users_all', UsersViewset, basename="users_all")
 
 
urlpatterns = [
    path('inventory/', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)