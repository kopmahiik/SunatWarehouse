from django.urls import path, include

from . import views

urlpatterns = [
    path(
        'products/', include([
            path(
                '',
                views.ProductViewSet.as_view(
                    {
                        'get': 'list',
                        'post': 'create',
                    }
                ),
            ),
            path(
                '<int:pk>/',
                views.ProductViewSet.as_view(
                    {
                        'get': 'retrieve',
                        'put': 'partial_update',
                        'delete': 'destroy',
                    }
                ),
            ),
        ])
    ),
]
