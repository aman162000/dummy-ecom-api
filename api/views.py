from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.http import JsonResponse
from .models import Product, Category
from fakeEcomAPIs.exceptions import CustomApiPermission
from rest_framework.authtoken.models import Token
from .serializer import ProductSerializer, CategorySerializer, LoginSerializer
from fakeEcomAPIs.filters import FiltersWhichAreNotProvidedByLibrary


class TokenLogin(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key}, status=200)


class CategoryData(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductData(generics.ListAPIView):
    # permission_classes = [CustomApiPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = FiltersWhichAreNotProvidedByLibrary
    ordering_fields = ['product_name', 'product_price']
