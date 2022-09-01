from django.urls import path

from . import views

app_name = 'short'

urlpatterns = [
    path('', views.ShortenerView.as_view(), name='makeshort'),
    path('url/<slug:short>/', views.RedirectUrl.as_view(), name='redirect')
]
