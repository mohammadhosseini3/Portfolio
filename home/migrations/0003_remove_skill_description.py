# Generated by Django 4.2.2 on 2023-09-16 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_person_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
    ]
