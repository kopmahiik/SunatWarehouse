from rest_framework.viewsets import ModelViewSet

from base.api_views import MultiSerializerViewSetMixin, DestroyFlagsModelMixin
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(
    MultiSerializerViewSetMixin,
    DestroyFlagsModelMixin,
    ModelViewSet
):
    queryset = Product.objects.get_available()
    serializer_action_classes = {
        'list': ProductSerializer,
        'retrieve': ProductSerializer,
        'create': ProductSerializer,
        'partial_update': ProductSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(self.request.user)
