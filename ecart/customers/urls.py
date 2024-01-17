from django.urls import path
from . import views

urlpatterns = [
    path("account", views.show_account, name="account"),
    path("logout", views.sign_out, name="logout"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
