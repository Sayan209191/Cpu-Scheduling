from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process-details/', views.process_details, name='process_details'),
]
