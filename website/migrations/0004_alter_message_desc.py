# Generated by Django 5.0.7 on 2024-07-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='desc',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
