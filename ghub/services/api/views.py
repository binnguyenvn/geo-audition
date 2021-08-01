from ghub.services.models import Service
from ghub.services.api.serializers import ServiceSerializer
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["name", "url", "description"]
    ordering_fields = "__all__"
    search_fields = ["name", "url", "description"]

    def list(self, request, *args, **kwargs):
        return super(ServiceViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ServiceViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ServiceViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ServiceViewSet, self).update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ServiceViewSet, self).delete(request, *args, **kwargs)
