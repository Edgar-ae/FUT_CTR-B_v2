# Generated by Django 4.2 on 2023-04-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='fut',
            name='binary_content',
            field=models.BinaryField(default=b''),
        ),
    ]
