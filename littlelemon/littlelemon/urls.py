
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from restaurant import views
router=DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),  # Homepage/Startpage 
    path('api/', include('restaurant.urls')),
    path('api/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

