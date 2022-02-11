from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero
from django.shortcuts import render
from django.http import HttpResponse



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


def myview(request):
    return HttpResponse("Hello There =)")

def process_view_test(request):
    return HttpResponse("Hello There =)")


