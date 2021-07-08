from django.shortcuts import render
from rest_framework.decorators import authentication_classes,api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import *
# Create your views here.

class TokenLogin(APIView):

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key},status=200)

@csrf_exempt
@api_view(["GET"])
def ProductDataAll(request):
    query = User.objects.get(username=request.user.username)
    serializer = UserSerializer(query)
    return JsonResponse(serializer.data, safe=False)
