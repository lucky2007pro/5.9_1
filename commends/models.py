from django.db import models

# Create your models here.

class Commend(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commend from {self.name} ({self.email})'

    class Meta:
        verbose_name = 'commend'
        verbose_name_plural = 'commends'