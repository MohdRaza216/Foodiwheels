# Generated by Django 5.0.7 on 2024-12-20 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_message_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='phone',
        ),
    ]
