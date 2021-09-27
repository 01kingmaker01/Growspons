from django.contrib.auth.models import User
from django.db import models

class Influencer(models.Model):
    influencer_id = models.OneToOneField(User, on_delete=models.CASCADE)