
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('programs', views.programs),
    path('about', views.about)

]