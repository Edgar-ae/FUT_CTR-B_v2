# Generated by Django 4.2 on 2023-04-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_fut_delete_fut_applicant_delete_fut_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fut',
            name='binary_content',
        ),
        migrations.AddField(
            model_name='fut',
            name='pdf_binary',
            field=models.BinaryField(default=b''),
        ),
        migrations.AddField(
            model_name='fut',
            name='qrimg_binary',
            field=models.BinaryField(default=b''),
        ),
    ]
