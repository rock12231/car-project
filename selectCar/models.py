from django.db import models
# Create your models here.

class ContactUs(models.Model):
    first_name = models.TextField(max_length=50,default='')
    last_name = models.TextField(max_length=50,default='')
    User_email = models.EmailField( max_length=50,default='')
    User_subject = models.TextField(max_length=100,default='')
    User_message = models.TextField( max_length=1000,default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User_email
