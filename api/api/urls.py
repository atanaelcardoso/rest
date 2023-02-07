from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet
from peso.views import ItemViewSet
from pro.views import ProdutoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'itens', ItemViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
