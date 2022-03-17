# Generated by Django 3.2.12 on 2022-03-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Enter title text', max_length=50, verbose_name='Name')),
                ('intro', models.CharField(max_length=250, verbose_name='Intro')),
                ('full_text', models.TextField(verbose_name='FullTXT')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
    ]
