# Generated by Django 3.0.7 on 2020-08-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
