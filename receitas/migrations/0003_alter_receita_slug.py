# Generated by Django 3.2.9 on 2021-12-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_alter_receita_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]