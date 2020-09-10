from django.db import models

# Create your models here.

class UserData(models.Model):
    userName = models.EmailField() # user Email
    userAge = models.IntegerField() # age of  the user 
    userCity = models.CharField(max_length=40)  # max length
    
    def __str__(self):
        return str(self.userName)


