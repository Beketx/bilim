from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

import datetime
import os
import uuid
import binascii
from bilim import settings

class UserManager(BaseUserManager):
    """Manager for creating Super user and Simple user"""
    def create_user(self, email, full_name, phone, password=None):
        if not email or not full_name or not phone:
            raise ValueError('Users required fields [email, full_name, phone]')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, full_name, phone, password):
        user = self.create_user(
            email,
            full_name,
            phone,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_activation(self, user, hash: str):
        return UserActivation.objects.create(
            user=user,
            code=hash
        )


class User(AbstractBaseUser):
    """Model of User, inherits from Django's AbstractBaseUser"""
    email = models.EmailField('eMail', unique=True, help_text='yourMail@bilim.kz')
    full_name = models.CharField('Name Surname', max_length=100, null=True)
    phone = models.CharField('Mobile phone', unique=True, max_length=12, help_text='77071113377',
                             null=True)
    photo = models.ImageField('Photo', upload_to='users', null=True, blank=True)
    created_at = models.DateTimeField('Date of registration', null=True, blank=True)
    is_active = models.BooleanField('Is active?', default=False)
    is_admin = models.BooleanField('Is admin?', default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserActivation(models.Model):
        """Model for user activation"""
        user = models.OneToOneField('authorize.User', on_delete=models.CASCADE,
                                    related_name='user_activation', verbose_name='User')
        code = models.CharField('Key', max_length=120, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        activated_at = models.DateTimeField(null=True, blank=True)

        def __str__(self):
            return "{} - {}".format(self.user, self.code)

        class Meta:
            verbose_name = 'Activation'
            verbose_name_plural = 'Activation'


