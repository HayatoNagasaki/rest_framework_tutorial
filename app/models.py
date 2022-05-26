from django.db import models


class MyModel(models.Model):
    number = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = "mytable"

    def __str__(self):
        return '{} | {}'.format(self.id, self.number)
