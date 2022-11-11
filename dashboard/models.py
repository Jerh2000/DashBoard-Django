from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORYGENDER = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

CATEGORYCITY = (
    ('Barranquilla', 'Barranquilla'),
    ('Bógota', 'Bógota'),
    ('Medellín', 'Medellín'),
    ('Cali', 'Cali'),
    ('Santa Marta', 'Santa Marta'),
    ('Amazonas', 'Amazonas'),
    ('Otros', 'Otros'),
    ('Internacional', 'Internacional'),
)

CATEGORYLEVEL = (
    ('Preescolar', 'Preescolar'),
    ('Básica Primaria', 'Básica Primaria'),
    ('Básica Secundaria', 'Básica Secundaria'),
    ('Media', 'Media'),
    ('Técnica', 'Técnica'),
    ('Tecnológica', 'Tecnológica'),
    ('Profesional', 'Profesional'),
)

class Flights(models.Model):
    year = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=255, choices=CATEGORYCITY)
    cantidad = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.year}'
    


class EducationLevel(models.Model):
    year = models.CharField(max_length=100, null=True)
    nivel = models.CharField(max_length=255, choices=CATEGORYLEVEL)
    cantidad = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.year}'
     
    
class Birth(models.Model):
    year = models.CharField(max_length=100, null=True)
    cantidad = models.PositiveIntegerField(null=True)
    categoria = models.CharField(max_length=255, choices=CATEGORYGENDER)

    def __str__(self):
        return f'{self.year}'
    



