from django.urls import path,include
from . import views

urlpatterns = [
    
    path('register/',views.register,name="register"),
    path('login/',views.UserLogin.as_view(),name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.userProfileView.as_view(),name="profile"),
    path('addEducation/',views.userEducation.as_view(),name="add_education"),
    # path('email_verifaction_sent/',views.send_verification_email,name="email_verification_sent"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    # path('verification/', include('verify_email.urls')),


]
