# Generated by Django 4.0.5 on 2022-07-25 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hablemosapp', '0030_alter_aboutus_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
    ]
