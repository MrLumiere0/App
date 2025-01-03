# Generated by Django 5.1.4 on 2024-12-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_democontactlist_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(max_length=30)),
                ('first_Name', models.CharField(max_length=30)),
                ('last_Name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Registered',
        ),
    ]
