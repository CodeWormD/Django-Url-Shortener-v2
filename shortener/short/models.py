from django.db import models
from .services import shortmaker


class Link(models.Model):
    url = models.URLField(unique=True)
    shorturl = models.CharField(unique=True, max_length=8)
    date = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    
    @classmethod
    def create(cls, link):
        short = shortmaker()
        try: 
            obj = cls.objects.create(url=link, shorturl=short)
        except Exception:
            obj = cls.objects.get(url=link)
        return obj