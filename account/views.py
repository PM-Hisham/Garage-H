from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import TemplateView,View,ListView,FormView,CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

class HomeView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("Username")
            pswd=form_data.cleaned_data.get("Password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"login successfull")
                return redirect('cc')
            else:
                messages.error(request,"sign in failed !! Please check you username and password")
                
                return redirect("h")
        return render(request,"chome.html",{"form":form_data})


class Regview(CreateView):
    template_name="reg.html"
    form_class=RegForm    
    model=User
    success_url=reverse_lazy("h")
    
    def form_valid(self,forms):
        messages.success(self.request,"Registeration successfull")
        return super().form_valid(forms)    
