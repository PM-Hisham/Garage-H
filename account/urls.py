from django.urls import path
from .views import *

urlpatterns = [
    path('reg',Regview.as_view(),name="re")
    
]