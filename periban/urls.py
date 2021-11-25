"""periban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from landing import views as landing_views
from menus import views as menu_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_views.home, name='home'),
    path('menu/', menu_views.menus, name="menus"),
    path('menu/<str:menu_name>/', menu_views.menu, name="menu"),
    path('menu/platillo/<str:name>/', menu_views.platillos, name="platillos"),
    path('servicio_domicilio/', landing_views.shipment, name="shipment"),
    path('cobertura/', landing_views.coverage, name="coverage"),
    path('sucursales/', landing_views.branches, name="branches"),
    path('eventos/', landing_views.events, name="events"),
    path('empleo/', landing_views.employees, name="employees"),
    path('medios/', landing_views.medios, name="medios"),
    path('facturacion/', landing_views.invoices, name="invoices"),
    path('aviso_privacidad/', landing_views.privacy_notice, name="privacy"),
    path('users/login/', landing_views.login_view, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
