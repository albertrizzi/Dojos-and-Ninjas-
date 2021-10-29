from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    description = models.TextField(default="")

    def __str__(self):
        return '{}'.format(self.name)


class Ninja(models.Model):

    dojo = models.ForeignKey(Dojo,
                            on_delete=models.CASCADE,
                            related_name='ninjas')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return '{}' '{}'.format(self.first_name , self.last_name)
