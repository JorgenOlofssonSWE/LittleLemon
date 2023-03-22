from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from .models import Booking,MenuItem
from .serializers import MenuItemSerializer,BookingSerializer

# Create your views here.

def index(request):
    print ('in views indec')
    return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
 


