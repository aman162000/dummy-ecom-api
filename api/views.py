from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from collections import OrderedDict
from rest_framework.decorators import permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .models import Product, Category
from fakeEcomAPIs.exceptions import CustomApiPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token, TokenProxy
from .serializer import ProductSerializer, CategorySerializer, LoginSerializer
from fakeEcomAPIs.filters import FiltersWhichAreNotProvidedByLibrary, CategoryFilter
from .users import Users

#TODO mRErvma8Brzh9B5
# TEST CI/CD
class TokenLogin(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key}, status=200)

class TokenLogout(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        Token.objects.get(user=request.user).delete()
        return Response({"message":"User Logged out successfully"}, status=200)

class CategoryData(generics.ListAPIView):
    permission_classes = [CustomApiPermission]
    serializer_class = CategorySerializer
    filter_class = CategoryFilter
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['category_name',]

    @method_decorator(cache_page(60*60*1))
    def dispatch(self, *args, **kwargs):
        return super(CategoryData,self).dispatch(*args,**kwargs)

class ProductData(generics.ListAPIView):
    permission_classes = [CustomApiPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = FiltersWhichAreNotProvidedByLibrary
    ordering_fields = ['product_name', 'product_price', 'product_sales']
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60*60*1))
    def dispatch(self, *args, **kwargs):
        return super(ProductData,self).dispatch(*args,**kwargs)

class UserData(APIView):
    permission_classes = [CustomApiPermission]

    def get(self,request):
        return JsonResponse(Users,safe=False)
