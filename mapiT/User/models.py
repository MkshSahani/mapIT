from django.db import models

# Create your models here.

class Friends(models.Model): # for list of the friend of a user. 
    keyPersonUserEmail = models.EmailField()  # the friend side 1.
    valuePersonUserEmail = models.EmailField()  # the friend side 2.
    friendSince = models.DateTimeField()  # when they become friends.

    def __str__(self):
        return str(self.keyPersonUserEmail + "_Friend_" + self.valuePersonUserEmail)  # get the relationship.
 