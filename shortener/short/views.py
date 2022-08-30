from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class ShortenerView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")
    
    def post(self, request, *args, **kwargs):
        pass