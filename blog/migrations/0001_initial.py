# Generated by Django 4.1.3 on 2022-11-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
