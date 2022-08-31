from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ShortForm
from .models import Link


class ShortenerView(View):
    
    def get(self, request, *args, **kwargs):
        form = ShortForm()
        context = {
            'form': form
        }
        return render(request, 'shortener.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ShortForm()
        url = request.POST.get('url', None)
        obj = Link.create(link=url)
        obj.save()
        context = {
            'form': form,
            'url': obj.url,
            'shorturl': request.get_host() + '/' + obj.shorturl
        }
        
        return render(request, 'shortener.html', context)


class RedirectUrl(View):
    
    def get(self, request, *args, **kwargs):
        pass