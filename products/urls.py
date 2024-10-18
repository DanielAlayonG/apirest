from django.urls import path
from .views import ProductoListCreateView, eliminar_producto

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', eliminar_producto, name='producto-delete'),
]