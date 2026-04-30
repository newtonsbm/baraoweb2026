"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app import views
from app.api import views as api_views 

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('padarias/', views.padarias_list, name='padarias_list'),
    path('cestas/', views.cestas_list, name='cestas_list'),
    path('cestas/<int:pk>/', views.cestas_detail, name='cestas_detail'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', views.dashboard_main, name='dashboard_main'),
    path('dashboard/perfil/', views.perfil_update, name='perfil_update'),
    path('receitas/buscar/', views.recipe_search, name='recipe_search'),
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('api/', api_views.api.urls), # Adiciona as rotas da API
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 