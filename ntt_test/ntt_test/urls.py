"""ntt_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from router.views import (
    routerList,
    createRouter,
    editRouter,
    deleteRouter,
    generateRecords,
    createRouterByApi,
    listRouterByApi,
    routerDetailApi,
)
from core import views as core_view
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'createRouterByApi', RouterViewSet)



urlpatterns = [
    path('', routerList, name="home"),
    path('signup/', core_view.signup, name="sign_up"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('createRouterByApi/', createRouterByApi),
    path('listRouterByApi/', listRouterByApi),
    path('routerDetailApi/<int:pk>/', routerDetailApi),
    path('create-router/', createRouter, name="create_router"),
    path('generateRecords/', generateRecords, name="generate_router"),
    url(r'^deleteRouter/$', deleteRouter, name="delete_router"),
    path('router/<int:pk>/', editRouter, name="edit_router"),
    path('admin/', admin.site.urls),
]
