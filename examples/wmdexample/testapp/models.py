from django.db import models

# Create your models here.

class Note(models.Model):
    """Test model
    """

    body = models.TextField()
