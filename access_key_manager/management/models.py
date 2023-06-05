from django.db import models

# Create your models here.
class Key(models.Model):
    status = models.CharField(max_length=10, choices=(
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked'),
    ))
    user_key = models.CharField(max_length=32, unique=True)
    date_of_procurement = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f'Key {self.id} for user {self.user.username}'
    
