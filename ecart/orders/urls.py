from django.urls import path
from . import views

urlpatterns = [
    path("cart", views.show_cart, name="cart"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
