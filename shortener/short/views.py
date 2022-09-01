from django.shortcuts import redirect, render
from django.views import View

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
        form = ShortForm(request.POST)
        if not form.is_valid():
            return render(request, 'shortener.html', {'form': form})
        else:
            url = request.POST.get('url', None)
            obj = Link.create(link=url)
            obj.save()
            context = {
                    'form': form,
                    'url': obj.url,
                    'shorturl': request.get_host() + '/url/' + obj.shorturl
                }
            return render(request, 'shortener.html', context)


class RedirectUrl(View):

    def get(self, request, *args, **kwargs):
        link = Link.objects.get(shorturl=kwargs['short'])
        link.count += 1
        link.save()
        return redirect(link.url)
