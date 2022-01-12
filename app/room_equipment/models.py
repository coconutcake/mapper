from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import DefaultObject
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError, FieldError


class ContainerType(DefaultObject, models.Model):

    """
    ContainerType
    """

    class Meta:
        verbose_name = _("Containertype")
        verbose_name_plural = _("Containertypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Containertype_detail", kwargs={"pk": self.pk})






class Container(DefaultObject, models.Model):

    """
    Container
    """

    container_type_fk = models.ForeignKey(
        ContainerType, verbose_name=_("container_type"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Container")
        verbose_name_plural = _("Containers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Container_detail", kwargs={"pk": self.pk})



class ContainerLevel(DefaultObject, models.Model):

    """
    ContainerType
    """
    
    container_fk = models.ForeignKey(
        Container, verbose_name=_("container"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Containerlevel")
        verbose_name_plural = _("Containerlevels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Containerlevel_detail", kwargs={"pk": self.pk})


class LocationType(DefaultObject, models.Model):

    """
    LocaltioType
    """

    class Meta:
        verbose_name = _("LocationType")
        verbose_name_plural = _("LocationTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LocationType_detail", kwargs={"pk": self.pk})




class Location(DefaultObject, models.Model):

    """
    ContainerType
    """
    
    container_level_fk = models.ForeignKey(
        Container, verbose_name=_("container_level"), on_delete=models.CASCADE)
    location_type = models.ForeignKey(
        LocationType, verbose_name=_("location_type"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})