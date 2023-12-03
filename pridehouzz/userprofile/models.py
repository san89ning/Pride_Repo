from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profile_image = models.ImageField(upload_to='uploads/profile_images/', blank=True, null=True)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    