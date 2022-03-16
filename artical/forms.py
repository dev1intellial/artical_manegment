from django.forms import ModelForm
from .models import Artical,Artical_Tag


class ArticalTageForm(ModelForm):
    class Meta:
        model=Artical_Tag
        fields=['tag']

class ArticalForm(ModelForm):
    class Meta:
        model=Artical
        exclude=['user_name','draf']
        