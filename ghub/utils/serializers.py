"""
    Base serializer
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from rest_framework.serializers import (CharField, DateTimeField, FileField,
                                        ModelSerializer, Serializer)

User = get_user_model()


class UserNestedViewSerializer(ModelSerializer):
    """
    User exclude password, username, email to update user profile
    """

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
        )


class BaseSerializer(ModelSerializer):
    """
    Base serializer
    """

    creator = UserNestedViewSerializer(read_only=True)
    last_modified_by = UserNestedViewSerializer(read_only=True)
    time_created = DateTimeField(format="%d-%m-%Y %H:%M", required=False)
    time_modified = DateTimeField(format="%d-%m-%Y %H:%M", required=False)

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(BaseSerializer, self).__init__(*args, **kwargs)
        try:
            fields = self.context["request"].query_params.get("fields")
            if fields:
                fields = fields.split(",")
                # Drop any fields that are not specified in the `fields` argument.
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
        except Exception:
            pass

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(BaseSerializer, self).get_field_names(
            declared_fields, info
        )
        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
