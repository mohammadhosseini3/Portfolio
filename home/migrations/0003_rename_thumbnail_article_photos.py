# Generated by Django 4.2.2 on 2023-09-11 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_person_github_link_person_instagram_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbnail',
            new_name='photos',
        ),
    ]