from django.db import models
# Create your models here.

class ContactUs(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    User_email = models.EmailField(null=False, max_length=254)
    User_subject = models.TextField(null=False)
    User_message = models.TextField(null=False, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.User_email
