# Generated by Django 2.0.2 on 2018-02-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Moto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais_origen', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='piloto',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moto.Nacionalidad'),
        ),
    ]
