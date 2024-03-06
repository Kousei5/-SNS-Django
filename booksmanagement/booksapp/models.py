from django.db import models
from django.utils import timezone

# Create your models here.



class BooksList(models.Model):
    STATUS_CHOICES = [
        ('unread', '未読'),
        ('read', '既読'),
    ]
    title = models.CharField(max_length=100)
    memo = models.TextField()
    read = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='unread'    
    )
    p_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title