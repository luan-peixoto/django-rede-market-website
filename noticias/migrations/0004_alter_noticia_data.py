# Generated by Django 3.2.9 on 2022-01-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.CharField(default='10/10/2020', max_length=50),
        ),
    ]
