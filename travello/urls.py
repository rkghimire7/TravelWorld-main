from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guide-availability/<int:guide_id>/', views.guide_availability, name='guide_availability'),
    path('book_guide/<int:guide_availability_id>/', views.book_guide, name='book_guide')

]