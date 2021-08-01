from common.models import APILog, GeneralSetting
from django.conf import settings


def newest_version(func):
    def wrap(*args, **kwargs):
        allowed = True
        setting = GeneralSetting.objects.filter(name="CRM_WORKER_VERSION").first()
        if setting is not None:
            version = setting.settings.get("version", None)
            if version is not None:
                # If CRM_WORKER_VERSION is config
                allowed = (
                    version == settings.VERSION
            )  # Allowed status based on config version and setting version
        if allowed:
            output = func(*args, **kwargs)
            return output
        else:
            try:
                APILog.objects.create(
                    content=f"Config {version} - Environtment {settings.VERSION} ",
                    endpoint="CELERY_WORKER",
                )
            except Exception:
                pass

    return wrap