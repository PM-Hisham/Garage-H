from django.urls import path
from .views import *

urlpatterns = [
    # path('c',Custhome.as_view(),name="ch"),
    path('ab',Custhome.as_view(),name="cc"),
    path('det/<int:id>',SerDetView.as_view(),name="dt"),
    path('userdata/<int:id>',PeriodicData.as_view(),name="userd"),
    path('carwash',CWashData.as_view(),name="cwash"),
    path('wheelallignment',WheelData.as_view(),name="wheel"),
    path('carpolish',PolishData.as_view(),name="polish"),
    path('bk',MyBooking.as_view(),name="mbk"),
    



 


    


]