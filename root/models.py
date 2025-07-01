from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.hashers import make_password
# Create your models here.
class Account(AbstractUser):
    pro_pic=models.ImageField(upload_to='pro_pic/')
    address=models.TextField(max_length=100)
    phone_no=models.CharField(max_length=10)

    def save(self,*args,**kwargs):
        self.set_password(self.password)
        super().save(*args,**kwargs)
        

    def __str__(self) -> str:
        return f'{self.username}'