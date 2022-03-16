from django.db import models
from authapp.models import Auth

class Artical(models.Model):
    user_name=models.ForeignKey(Auth,on_delete=models.CASCADE,default=False)
    artical_imaga=models.ImageField(upload_to='image')
    tital=models.CharField(max_length=100)
    content=models.TextField(max_length=5000)
    draf=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}{self.tital}'

class Artical_Tag(models.Model):
    artical=models.ForeignKey(Artical,on_delete=models.CASCADE)
    tag=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}{self.tag}'

class Tag(models.Model):
    tags=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tags}'