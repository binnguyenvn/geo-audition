from ghub.services.models import Service
from ghub.utils.serializers import BaseSerializer


class ServiceSerializer(BaseSerializer):
    class Meta:
        model = Service
        fields = ["name", "url", "description"]
