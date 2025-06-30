from django.db import models
from django.core.validators import RegexValidator

no_spaces_validator =RegexValidator(
    regex=r'^\S+$',
    message='Espaços não são permitidos.'
)

class User(models.Model):
    name = models.CharField(
        max_length=255 ,
        verbose_name="Nome",
        blank=False,
        null=False
        )
    
    password = models.CharField(
        max_length=20,
    )

    sur_name = models.CharField(
        max_length=255 ,
        verbose_name="Sobrenome",
        blank=True,
        null=True
        )

    user_name = models.CharField(
        max_length=255,
        verbose_name='Usuário',
        validators=[no_spaces_validator],
        unique=True,
        blank=False,
        null=False
    )
    
    email = models.EmailField(
        max_length=255,
        verbose_name="E-mail",
        unique=True,
        blank=False,
        null=False
    )
    age = models.DateField(
        max_length=255,
        verbose_name='Data Nascimento',
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Usuário'

    def __str__(self):
        return f'{self.name} {self.sur_name}'