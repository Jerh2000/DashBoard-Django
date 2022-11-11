# Generated by Django 3.2 on 2022-10-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('categoria', models.CharField(choices=[('Vivo', 'Vivo'), ('Muerto', 'Muerto')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('categoria', models.CharField(choices=[('Resto de ciertas enfermedades infecciosas y parasitarias', 'Resto de ciertas enfermedades infecciosas y parasitarias'), ('Otras causas', 'Otras causas')], max_length=255, null=True)),
            ],
        ),
    ]
