from django.db import models


class Recipient(models.Model):
    email = models.EmailField(max_length=125, verbose_name='Email Address')
    full_name = models.CharField(max_length=125, verbose_name='Full Name')
    score = models.IntegerField(default=1, verbose_name='Score')

    def __str__(self):
        return f'{self.id} | {self.full_name}'
