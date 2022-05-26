from django.contrib.auth.models import User
from django.db import models


class TestModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.id, self.number)
