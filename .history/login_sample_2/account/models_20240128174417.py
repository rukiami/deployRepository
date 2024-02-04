from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
    
from django.db import models

class Event(models.Model):
    # ここにフィールドを定義します
    title = models.CharField(max_length=200)
    date = models.DateField()
    image_url = models.URLField(blank=True, null=True)
    store_link = models.URLField(blank=True, null=True)
    map_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
    # some_field_name  # 'title' フィールドがあると仮定    
