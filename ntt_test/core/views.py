from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import response, decorators, permissions, status
from .serializers import UserCreateSerializer
from django.contrib.auth import login, authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def signup(request, *args, **kwargs):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()

    refresh = RefreshToken.for_user(user)

    res = {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

    return Response(res, status.HTTP_201_CREATED)

