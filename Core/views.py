from verify_email.email_handler import send_verification_email
from django.shortcuts import render,redirect
from . import forms

from django.views.generic import FormView,TemplateView
# Create your views here.
from . import forms
from Tution.models import Application
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View


# def register(request):
#     if request.method=='POST':
#         register_form=forms.regirtrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request,'account created succesfully')
#     else:
#         register_form=forms.regirtrationForm()
#     return render(request,'register.html',{'form':register_form,'type':'register'})

class UserAccountRegistrationView(FormView):
    template_name='register.html'
    form_class=forms.UserAccountRegistrationForm
    success_url=reverse_lazy('homepage')
    
    def form_valid(self,form):
        inactive_user = send_verification_email(self.request, form)
        print('in account form valid')
        user=form.save()
        login(self.request,user)
        return super().form_valid(form) # form_valid function call hobhe jodi sohb thik thake


class UserLogin(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
        

def user_logout(request):
    logout(request)
    return redirect('login')


class userProfileView (TemplateView):
    template_name='profile.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=forms.UserUpdateForm(instance=self.request.user)
        context['approved_applications']=Application.objects.filter(user=self.request.user,is_approved=True)
        return context
    
    def post (self,request,*args,**kwargs):
        form=forms.UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        return self.render_to_response(self.get_context_data())