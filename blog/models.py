from django.db import models

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Título',
        blank=False,
        null=False,
    )

    description = models.TextField(
        verbose_name='Texto',
        blank=False,
        null=False,
    )

    autor = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        verbose_name="Autor",
        null=True
    )

    date = models.DateField(
        verbose_name='Data',
        auto_now=True,
    )

class Reaction(models.Model):
    text_reaction = models.TextField(
        blank=False,
        null=False
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
    )

    date = models.DateField(
        verbose_name='Data',
        auto_now=True,
        null=False
    )
