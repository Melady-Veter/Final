from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('имя', max_length=120, blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=240, blank=True, null=True)
    email = models.EmailField('email')

    def __str__(self):
        return "Профиль пользователя %s" % self.user

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
