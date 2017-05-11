from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return self.user.username

    @property
    def products(self):
        return self.product_set.all()

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Account.objects.create(user=instance)

class Product(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    serial = models.CharField(max_length=40)
    account = models.ForeignKey(Account)
    end_date = models.DateTimeField()
