# draw_member/models.py
from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=256, unique=True)
    drawed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
