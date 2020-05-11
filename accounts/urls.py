from django.urls import path
from . import views
 
urlpatterns = [
    path('signup/', views.SignUpView, name='signup'), 
    path('activate/<uidb64>/<token>/', views.Activate, name='activate'),

    path('signin/', views.SignInView, name='signin'), 
  
    path('profile/', views.ProfileView, name='profile'),  
]
