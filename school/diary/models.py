from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class lesson(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название")
    
    description = models.CharField(
        max_length=255, verbose_name="Описание"
        )

    teacher = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="teacher"
        )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Учитель"
    )
    