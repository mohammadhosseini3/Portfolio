# Generated by Django 4.2.2 on 2023-09-10 16:00

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('summary', models.CharField(max_length=500, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50, null=True)),
                ('university', models.CharField(max_length=50, null=True)),
                ('started_at', models.DateField(null=True)),
                ('ended_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=home.models.change_img_name)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkedAt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('created_at', models.DateField(null=True, verbose_name='Careted At')),
                ('img', models.ManyToManyField(blank=True, to='home.image')),
                ('tag', models.ManyToManyField(blank=True, to='home.projecttag')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=50, null=True, verbose_name='first name')),
                ('lname', models.CharField(blank=True, max_length=50, null=True, verbose_name='last name')),
                ('biography', models.TextField(max_length=500, null=True)),
                ('client_number', models.IntegerField(null=True)),
                ('years_of_experience', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('bdate', models.DateField(null=True, verbose_name='birth date')),
                ('article', models.ManyToManyField(blank=True, to='home.article')),
                ('education', models.ManyToManyField(blank=True, to='home.education')),
                ('img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.image')),
                ('project', models.ManyToManyField(blank=True, to='home.project')),
                ('skill', models.ManyToManyField(blank=True, to='home.skill')),
                ('worked_at', models.ManyToManyField(blank=True, to='home.workedat')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ManyToManyField(blank=True, to='home.image'),
        ),
    ]
