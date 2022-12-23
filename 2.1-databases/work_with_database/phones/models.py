from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=200)

