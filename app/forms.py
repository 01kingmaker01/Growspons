from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'first_name', 'password1', 'password2']

class InfluencerForm(ModelForm):
    class Meta:
        model=Influencer
        fields='__all__'