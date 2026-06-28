from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Profiles")
    id_user = models.AutoField(primary_key=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username



