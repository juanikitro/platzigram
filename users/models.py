"""User models"""

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model

    Proxy model that expends the base data with other information
    """

    user = models.OneToOneField(User, on_delete = models.CASCADE) # 1:1

    website = models.URLField(blank=True, max_length = 200)
    biography = models.TextField(blank = True)
    phone_number = models.CharField(blank = True, max_length = 20)
    picture = models.ImageField(
            blank = True, 
            upload_to = 'users/pictures', 
            null = True
        )

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        """Returns username"""
        return self.user.username