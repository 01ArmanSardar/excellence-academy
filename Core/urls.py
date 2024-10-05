from django.urls import path,include
from . import views

urlpatterns = [
    
    path('register/',views.UserAccountRegistrationView.as_view(),name="register"),
    path('login/',views.UserLogin.as_view(),name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.userProfileView.as_view(),name="profile"),
     path('verification/', include('verify_email.urls')),

]
