# Generated by Django 3.2.9 on 2022-01-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='desc_full',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='desc_mini',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.CharField(max_length=50),
        ),
    ]
