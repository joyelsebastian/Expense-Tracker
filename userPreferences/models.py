from django.db import models
from django.contrib.auth.models import User

class UserPreferences(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    currency=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self) -> str:
        return str(self.user) + 's' + 'preferences' 