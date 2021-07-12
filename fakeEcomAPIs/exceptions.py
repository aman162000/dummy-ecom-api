from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey, BaseHasAPIKey, KeyParser
from rest_framework.exceptions import APIException
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
import typing

# CustomException is used to get "Please provide API key" message when API key is not provided.
class CustomException(APIException):
    status_code = 406
    default_detail = _('Please provide valid API key.')
    default_code = _('please provide api key.')

# Override Permission class of Rest framework
class CustomApiPermission(permissions.BasePermission):
    model = APIKey

    key_parser = KeyParser()

    def get_key(self, request: HttpRequest) -> typing.Optional[str]:
        return self.key_parser.get(request)

    def has_permission(self, request: HttpRequest, view: typing.Any) -> bool:
        key = self.get_key(request)
        if not key:
            raise CustomException()
        if not self.model.objects.is_valid(key):
            raise CustomException()

        return self.model.objects.is_valid(key)