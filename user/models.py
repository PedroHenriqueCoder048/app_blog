import os
from django.db import models
from django.core.validators import RegexValidator
from .emails.base import Email


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

    def account_confirmatiom(self):
        subject = "TESTE DE CONFIRMAÇÃO DE CONTA"
        message = "Confirmação de conta \n esse email é um teste para confirmar sua conta"
        from_email = os.environ.get('EMAIL_HOST_USER')
        to_emails = [self.email]
        
        email = Email(
            subject,
            message,
            from_email,
            to_emails
        )

        email.send_email()

    def recover_password(self):
        subject = "Teste de Recuperação de senha"
        message = f"email para recuperar sua senha\nSua senha é :{self.password}"
        from_email = os.environ.get('EMAIL_HOST_USER')
        to_emails = [self.email]
        
        email = Email(
            subject,
            message,
            from_email,
            to_emails
        )

        email.send_email()

    class Meta:
        ordering = ['name']
        verbose_name = 'Usuário'

    def __str__(self):
        return f'{self.name} {self.sur_name}'