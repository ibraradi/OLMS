# Generated by Django 5.1.1 on 2024-09-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/profile_pics/'),
        ),
    ]
