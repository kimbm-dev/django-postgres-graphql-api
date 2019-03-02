"""commons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from graphene_django.views import GraphQLView
from django.contrib.auth import views
from django.views.decorators.csrf import csrf_exempt
from commons.schema import schema

urlpatterns = [
    # path('password_reset/', views.PasswordResetView.as_view(), name='admin_password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
    # path(r'graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    # path(r'__graphiql/', GraphQLView.as_view(graphiql=True)),
    url(r'^__graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^__graphiql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
