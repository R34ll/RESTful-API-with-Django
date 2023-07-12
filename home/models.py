from datetime import datetime
from django.db import models


ROLES = [
    "Administrator",
    "Developer",
    "Design"
]


class User(models.Model):

    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    status = models.BooleanField(default=True) 
    
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username


