from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('education/', views.education_list, name='education'),
]