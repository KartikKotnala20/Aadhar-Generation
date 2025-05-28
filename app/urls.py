from django.urls import path
from . import views

urlpatterns = [
    path('',views.Hero,name='hero'),
    path('create/',views.Index,name='index'),
    path('download/',views.Download,name='download'),
    # path('display/',views.Download,name='display')
]
