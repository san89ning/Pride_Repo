from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 50, blank=True)
    last_name = models.CharField(max_length = 50, blank=True)
    email_address = models.EmailField(max_length = 150, blank=True)
    message = models.CharField(max_length = 150, blank=True)

    def __str__(self):
        return self.first_name
    