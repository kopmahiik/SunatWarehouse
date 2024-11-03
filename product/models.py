from django.db import models

from base.models import TimeStampedFlagsModel


class Product(TimeStampedFlagsModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['id']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

