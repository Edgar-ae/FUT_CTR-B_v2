# Generated by Django 4.2 on 2023-04-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_fut_applicant_fut_record_delete_fut_delete_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='fut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('cycle', models.CharField(max_length=2)),
                ('myrequest', models.TextField()),
                ('order', models.CharField(max_length=300)),
                ('reason', models.TextField()),
                ('date', models.DateField()),
                ('binary_content', models.BinaryField(default=b'')),
                ('proceeding', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='fut_applicant',
        ),
        migrations.DeleteModel(
            name='fut_record',
        ),
    ]