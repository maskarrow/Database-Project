from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("clienti/", views.clienti_list, name="clienti_list"),
    path("clienti/add/", views.clienti_create, name="clienti_add"),
    path("clienti/<int:pk>/edit/", views.clienti_update, name="clienti_edit"),
    path("clienti/<int:pk>/delete/", views.clienti_delete, name="clienti_delete"),

    path("produse/", views.produse_list, name="produse_list"),
    path("produse/add/", views.produse_create, name="produse_add"),
    path("produse/<int:pk>/edit/", views.produse_update, name="produse_edit"),
    path("produse/<int:pk>/delete/", views.produse_delete, name="produse_delete"),

    path("producatori/", views.producatori_list, name="producatori_list"),
    path("producatori/add/", views.producatori_create, name="producatori_add"),
    path("producatori/<int:pk>/edit/", views.producatori_update, name="producatori_edit"),
    path("producatori/<int:pk>/delete/", views.producatori_delete, name="producatori_delete"),

    path("relatii/client-produs/", views.client_produs_list, name="client_produs_list"),
    path("relatii/client-produs/add/", views.client_produs_create, name="client_produs_add"),
    path("relatii/client-produs/<int:pk>/edit/", views.client_produs_update, name="client_produs_edit"),
    path("relatii/client-produs/<int:pk>/delete/", views.client_produs_delete, name="client_produs_delete"),

    path("relatii/produs-producator/", views.produs_producator_list, name="produs_producator_list"),
    path("relatii/produs-producator/add/", views.produs_producator_create, name="produs_producator_add"),
    path("relatii/produs-producator/<int:pk>/edit/", views.produs_producator_update, name="produs_producator_edit"),
    path("relatii/produs-producator/<int:pk>/delete/", views.produs_producator_delete, name="produs_producator_delete"),
]
