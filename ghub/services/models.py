from ghub.utils.models import BaseModel
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Service(BaseModel):
    """Service for Geo's Hub."""

    name = CharField(_("Name of Service"), blank=True, max_length=255)
    url = CharField(_("Slug of Service"), blank=True, max_length=255)
    description = CharField(_("Description of Service"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for service's detail view.

        Returns:
            str: URL for service detail.

        """
        return reverse("api:service-detail", kwargs={"pk": self.pk})
