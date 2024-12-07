from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductoViewSet  # Asegúrate de que el nombre del ViewSet esté correcto
from django.shortcuts import redirect

# Crear el router y registrar el ViewSet
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)  # Ruta para el ViewSet de productos

# Configuración de las URLs
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del admin de Django
    path('api/', include(router.urls)),  # Ruta de la API para productos
    path('', lambda request: redirect('/api/')),  # Redirige la raíz a /api/
]


