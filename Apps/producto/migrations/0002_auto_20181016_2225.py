# Generated by Django 2.0.6 on 2018-10-16 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='tipo_art',
            field=models.CharField(max_length=60),
        ),
    ]