# Generated by Django 3.2.9 on 2022-01-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20220104_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateField(),
        ),
    ]