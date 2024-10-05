# from verify_email.email_handler import send_verification_email
from django.shortcuts import render,redirect
from . import forms

from django.views.generic import FormView,TemplateView
# Create your views here.
from . import forms
from Tution.models import Application
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.urls import reverse
from .forms import UserRegistrationForm
# from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View


def register(request):
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.is_active= False
            user.save()

            #send email verification
            current_site=get_current_site(request)
            mail_subject='Active your tution media platfrom account'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            activation_link = reverse('activate',kwargs={'uidb64':uid, 'token':token})
            activation_url = f'http://{current_site.domain}{activation_link}'

            message =render_to_string('email_verifaction.html',{
                'user':user,
                'activation_url':activation_url,
            })
            send_mail(mail_subject,message,'armansardar0109@gmail.com',[user.email])
            return redirect('profile')
    else:
        form=forms.UserRegistrationForm()
    return render(request,'register.html',{'form':form,'type':'register'})

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return redirect('profile')
    else:
        return render(request,'activation_invalid.html')

# class UserAccountRegistrationView(FormView):
#     template_name='register.html'
#     form_class=forms.UserAccountRegistrationForm
#     success_url=reverse_lazy('homepage')
    
#     def form_valid(self,form):
#         inactive_user = send_verification_email(self.request, form)
#         print('in account form valid')
#         user=form.save()
#         login(self.request,user)
#         return super().form_valid(form) # form_valid function call hobhe jodi sohb thik thake


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