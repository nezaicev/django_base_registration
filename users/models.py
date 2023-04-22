from django.core.validators import RegexValidator
from django.core.mail import send_mail, mail_admins
from django.utils.text import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from users.managers import CustomAccountManager


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField('email', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    postal_code = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))], )
    city = models.CharField('Город', max_length=150)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = ()

    def save(self, *args, **kwargs):
        if not self.pk:
            mail_admins('new user',
                        'new_user: {}'.format(self.email))
            send_mail('Registration', 'You login {}'.format(self.email), 'admin@domen.ru',
                      [self.email], )
        super(CustomUser, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
