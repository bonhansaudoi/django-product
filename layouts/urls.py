from django.urls import path
from . import views
 
urlpatterns = [  
    path('', views.IntroView.as_view(), name='home'),

    path('contact/', views.ContactView, name='contact'),
    path('success/', views.SuccessView, name='success'),
] 