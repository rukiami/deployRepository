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
    date = models.DateField()
    image_url = models.URLField()
    store_link = models.URLField()
    map_info = models.TextField()

    def __str__(self):
        return self.some_field_name  # 'title' フィールドがあると仮定    
