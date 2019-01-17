from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Liquor(models.Model):
    name = models.CharField(max_length=200)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
