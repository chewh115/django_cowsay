from django.urls import path
from django_cowsay import views

urlpatterns = [
    path('', views.index, name='homepage'),
    # path('history/', views.history, name='history')
]