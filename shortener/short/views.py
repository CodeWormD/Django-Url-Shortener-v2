from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ShortForm

class ShortenerView(View):
    
    def get(self, request, *args, **kwargs):
        form = ShortForm()
        context = {
            'form': form
        }
        return render(request, 'shortener.html', context)
    
    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello World")


class RedirectUrl(View):
    
    def get(self, request, *args, **kwargs):
        pass