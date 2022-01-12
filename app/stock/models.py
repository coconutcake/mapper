from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError
import room_equipment.models

class Item(DefaultObject, models.Model):

    """
    Item
    """

    location_fk = models.ForeignKey(
        room_equipment.models.Location, 
        verbose_name=_("location"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
