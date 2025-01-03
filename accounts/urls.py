from  django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('guides/', views.guides, name='guides'),
    path('guide/', views.guide, name='guide'),  # Added forward slash
    path('destinations/', views.destinations, name='destinations'),
]