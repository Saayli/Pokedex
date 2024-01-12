from django.db import models


class Pokemon(models.Model):
    id_pokemon = models.IntegerField(default=1)
    name = models.CharField(max_length=30)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    img = models.CharField(max_length=300)
    types = models.JSONField
    description = models.CharField(max_length=300)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

