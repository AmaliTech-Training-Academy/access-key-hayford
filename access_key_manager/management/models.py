from django.db import models
from account.models import CustomUser

# Create your models here.
class Key(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked'),
    ))
    key = models.CharField(max_length=32, unique=True)
    date_of_procurement = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    school = models.ForeignKey('School', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.status}{self.key}{self.expiry_date}{self.date_of_procurement}{self.school}{self.user.username}'

    # def __str__(self):
    #     return f'Key {self.id} for user {self.user.username}'
    
    def get_username(self):
        return self.user.username
    

class School(models.Model):
    name= models.CharField(max_length= 255)
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    
