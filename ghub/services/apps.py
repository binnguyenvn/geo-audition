from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServicesConfig(AppConfig):
    name = "ghub.services"
    verbose_name = _("Services")

    def ready(self):
        try:
            import ghub.services.signals  # noqa F401
        except ImportError:
            pass
