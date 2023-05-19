from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import User

# Create your models here


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    message = models.TextField()
    form_field1 = models.CharField(max_length=100)
    form_field2 = models.IntegerField()

    #class Meta:
    #    app_label = 'myapp'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    def __str__(self):
        return "A " + self.message + self.position + " from: " + str(self.user)

    #class Meta:
    #    app_label = 'myapp'


class Notification2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    def __str__(self):
        return "A " + self.message + self.position + " from: " + str(self.user)

    
class Notification3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    def __str__(self):
        return "A " + self.message + self.position + " from: " + str(self.user)



#class UserProfile(AbstractServer):
#    # add any additional fields you want
#    # example: address = models.CharField(max_length=255)
#    pass