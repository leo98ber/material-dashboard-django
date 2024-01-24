# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class SubscriptionLevel(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name



class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=16)
    activation_date = models.DateField(auto_now_add=True)
    preferences = models.TextField()
    level = models.ForeignKey(SubscriptionLevel,
                              on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Subscription of {self.user.username}"


@receiver(post_migrate)
def create_default_subscription_levels(sender, **kwargs):
    if sender.name == 'apps.home':
        model = sender.get_model('SubscriptionLevel')
        if not model.objects.exists():
            model.objects.create(name='Nivel 1', level='1')
            model.objects.create(name='Nivel 2', level='2')
            model.objects.create(name='Nivel 3', level='3')
