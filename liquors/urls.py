from django.urls import path
from . import views

app_name = 'liquors'
urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
]
