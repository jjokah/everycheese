from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "HARD"

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True,
                         always_update=False,
                         populate_from="name")
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Firmness",
                                max_length=20,
                                choices=Firmness.choices,
                                default=Firmness.UNSPECIFIED)

    def __str__(self):
        return self.name
