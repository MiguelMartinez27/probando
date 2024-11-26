from django.contrib import admin
from django.urls import path
from Inmuebles.views import (
    perfil_usuario,
    registro_usuario,
    home,
    lista_inmuebles_por_region,
    detalle_inmueble,
    MiInmueblesListView,
    MiInmueblesDetailView,
    MiInmueblesCreateView,
    MiInmueblesUpdateView,
    MiInmueblesDeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registro/", registro_usuario, name="registro"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("", home, name="home"),
    path(
        "region/<int:region_id>/inmuebles/",
        lista_inmuebles_por_region,
        name="lista_inmuebles_por_region",
    ),
    path("inmueble/<int:pk>/", MiInmueblesDetailView.as_view(), name="vista_inmueble"),
    path("inmuebles/", MiInmueblesListView.as_view(), name="inmuebles_list"),
    path("inmuebles/nuevo/", MiInmueblesCreateView.as_view(), name="inmueble_creacion"),
    path(
        "inmuebles/<int:pk>/editar/",
        MiInmueblesUpdateView.as_view(),
        name="inmueble_form",
    ),
    path(
        "inmuebles/<int:pk>/eliminar/",
        MiInmueblesDeleteView.as_view(),
        name="inmueble_eliminar",
    ),
    path("inmueble/<int:id>/", detalle_inmueble, name="detalle_inmueble"),
    path("perfil/", perfil_usuario, name="perfil_usuario"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
