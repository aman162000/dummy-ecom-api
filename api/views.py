from rest_framework.decorators import api_view, permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.http import JsonResponse
from .models import *
from fakeEcomAPIs.exceptions import CustomApiPermission
from rest_framework.authtoken.models import Token
from .serializer import *


# Create your views here.

class TokenLogin(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key}, status=200)


@api_view(["GET"])
@permission_classes([CustomApiPermission])
@cache_page(60)
def ProductDataAll(request):
    query = Product.objects.all()
    serializer = ProductSerializer(query, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def addData():
    pass