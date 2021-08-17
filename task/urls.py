from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about/',views.ainul),
     path('update/<id>', views.ainul),
     path('about/<id>', views.ainul),
     
]