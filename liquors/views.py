from django.shortcuts import render

from django.views import generic
from .models import Liquor

class ListView(generic.ListView):
    model = Liquor
