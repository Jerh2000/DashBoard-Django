# Generated by Django 4.0.4 on 2022-11-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_flights'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Death',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.RemoveField(
            model_name='birth',
            name='categoria',
        ),
        migrations.AddField(
            model_name='birth',
            name='gender',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=255, null=True),
        ),
    ]
