# Generated by Django 3.2.6 on 2021-10-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='address1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='area',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='phn',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='postcode',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='region',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
