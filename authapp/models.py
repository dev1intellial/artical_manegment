from django.db import models
from django.contrib.auth.models import AbstractUser


class Auth(AbstractUser):
    pass
    
    def __str__(self):
        return f'{self.username}'


