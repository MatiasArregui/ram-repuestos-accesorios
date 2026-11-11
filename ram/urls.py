
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

import os

urlpatterns = [

    path('admin/', admin.site.urls),

    # LOGIN
    path(
        'login/',
        LoginView.as_view(
            template_name=os.path.join(
                "carga", "forms", "login.html"
            ),
            authentication_form=LoginForm
        ),
        name='ingreso'
    ),

    # LOGOUT
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # APLICACIÓN TIENDA
    path('', include('tienda.urls')),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


