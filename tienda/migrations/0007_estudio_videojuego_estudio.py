# Generated by Django 4.2.2 on 2023-06-28 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_rename_categoria_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='videojuego',
            name='estudio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.estudio'),
            preserve_default=False,
        ),
    ]
