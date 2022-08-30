from django.db import models



class Link(models.Model):
    url = models.URLField(unique=True)
    shorturl = models.CharField(unique=True, max_length=8)
    date = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)
    
    