from django.urls import path
from . import views

app_name = 'short'

urlpatterns = [
    path('', views.ShortenerView.as_view(), name='makeshort')
]