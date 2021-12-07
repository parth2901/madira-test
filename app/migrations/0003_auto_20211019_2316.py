# Generated by Django 3.2.5 on 2021-10-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='country',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='state',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='zipcode',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]