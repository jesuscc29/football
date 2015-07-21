# coding=utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Player(models.Model):
    POSITIONS = (
        (0, 'No Definido'),
        (1, 'Portero'),
        (2, 'Defensa'),
        (3, 'Medio'),
        (4, 'Delantero')
    )
    name = models.CharField(verbose_name='Nombre', max_length=255)
    number = models.SmallIntegerField(verbose_name='Número',
                                      max_length=3, blank=True, null=True)
    position = models.SmallIntegerField(verbose_name='Posición',
                                        max_length=1, default=0,
                                        choices=POSITIONS, blank=True, null=True)
    picture = models.ImageField(verbose_name='Foto', blank=True, null=True,
                                upload_to='pictures')

    def __str__(self):
        return ' '.join([self.name, str(self.number)])