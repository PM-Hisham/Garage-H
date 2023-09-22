from django.shortcuts import render,redirect
# from .forms import *
from django.views.generic import TemplateView,View,ListView,FormView,CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from account.models import Services,Book
# Create your views here.




class Custhome(ListView):
    template_name="chome.html"
    queryset=Services.objects.all()
    context_object_name="service"


class SerDetView(DetailView):
    template_name="details.html"
    pk_url_kwarg="id"
    queryset=Services.objects.all()
    context_object_name="data"   

 
class PeriodicData(TemplateView):
    template_name="periodic.html"

    def post(self, request, **kwargs):
        id = kwargs.get("id")
        services=Services.objects.get(id=id)
        user = request.user
        name=request.POST.get("nme")
        timeslot = request.POST.get("ts")
        date = request.POST.get("dt")
        phone=request.POST.get("phn")
        address=request.POST.get("add")
        fuel_type=request.POST.get("ftype")

        book = Book(user=user, timeslot=timeslot, date=date,services=services,phone=phone,address=address,fuel_type=fuel_type,name=name)
        book.save()
        
        messages.success(request, "Booking successful")

        return redirect("mbk")
    

# class BookView(TemplateView):
#     template_name="book.html"

#     def post(self,request,**kwargs):
#         id = kwargs.get("id")
#         services=Services.objects.get(id=id)
#         user=request.user
#         phone=request.POST.get("phn")
#         address=request.POST.get("add")
#         fuel_type=request.POST.get("ftype")
#         Book.objects.create(services=services,user=user,phone=phone,address=address,fuel_type=fuel_type)
#         services.save()
#         messages.success(request,"Booking successfull !!")
#         return redirect("mbk")


        

        



class CWashData(TemplateView):
    template_name="carwash.html"
   
class WheelData(TemplateView):
    template_name="wheel.html"
   
class PolishData(TemplateView):
    template_name="polish.html"





class MyBooking(ListView):
    template_name="My bookings.html"
    queryset=Book.objects.all()
    context_object_name="book"   
   
   

    


       