# Generated by Django 4.0.4 on 2022-05-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectCar', '0008_remove_contactus_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='User_email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contactus',
            name='User_message',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='contactus',
            name='User_subject',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contactus',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='first_name',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contactus',
            name='last_name',
            field=models.TextField(default='', max_length=50),
        ),
    ]
