# Generated by Django 4.2.2 on 2023-09-07 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_person_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.image'),
        ),
    ]