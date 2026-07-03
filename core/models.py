from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
import uuid
import datetime
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Profiles")
    id_user = models.AutoField(primary_key=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Post"