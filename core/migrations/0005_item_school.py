# Generated by Django 2.2.10 on 2020-03-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='school',
            field=models.CharField(choices=[('A', 'School A'), ('F', 'School F'), ('C', 'School C')], default='school', max_length=2),
        ),
    ]
