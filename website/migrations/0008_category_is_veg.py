# Generated by Django 5.0.7 on 2024-12-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_category_options_alter_fooditem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_veg',
            field=models.BooleanField(default=True),
        ),
    ]