# Generated by Django 4.2.2 on 2023-07-10 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0022_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='titulo',
        ),
    ]
