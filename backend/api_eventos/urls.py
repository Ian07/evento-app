"""api_eventos URL Configuration

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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
from api_eventos.views import MyTokenObtainPairView
from .views import home, send_push
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('participantes.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('cursos.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # Estas corresponden a la parte de Web Push
    path('', home),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + 
