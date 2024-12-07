from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Obtiene todos los productos
    serializer_class = ProductoSerializer  # Utiliza el serializer para convertir el modelo en JSON

