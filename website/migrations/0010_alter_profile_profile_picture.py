# Generated by Django 5.0.7 on 2024-12-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_message_email_alter_fooditem_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default_profile.png', upload_to='profile_pictures/'),
        ),
    ]
