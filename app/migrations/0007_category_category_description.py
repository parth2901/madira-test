# Generated by Django 3.2.5 on 2021-10-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_addaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
