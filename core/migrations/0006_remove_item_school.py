# Generated by Django 2.2.10 on 2020-03-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='school',
        ),
    ]
