"""
URL configuration for TankYou project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from users import views as user_views
from vehicles import views as vehicle_views
from users.views import UsersHomeView
from vehicles.views import VehiclesHomeView
from orders.views import OrdersHomeView
from recharges.views import RechargesHomeView
from payments.views import PaymentsHomeView
from notifications.views import NotificationsHomeView
from users.views import UsersListView
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from users.api.views import UsuarioCRUDView, UsuarioViewSet

# Direcciones de la API REST (Esto recibe la url api/)
router = DefaultRouter()
router.register('usuarios_list', UsuarioViewSet, basename='usuarios')
router.register('usuarios_crud', UsuarioCRUDView, basename='usuarios-crud')

urlpatterns = [
    
    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', user_views.HomeView.as_view(), name='Home'),

    # USERS
    path("users/", UsersListView.as_view(), name="usuarios_lista"),
    path('usuarios/crear/', user_views.UserCreateView.as_view(), name='usuario_crear'),
    path('usuarios/editar/<int:pk>/', user_views.ProyectoUpdateView.as_view(), name='usuario_editar'),
    path('usuarios/eliminar/<int:pk>/', user_views.ProyectoDeleteView.as_view(), name='usuario_eliminar'),

    # VEHICLES
    path("vehicles/", vehicle_views.VehiclesHomeView.as_view(), name="vehicles"),
    path("vehicles/crear/", vehicle_views.VehiclesCreateView.as_view(), name="vehiculo_crear"),
    path("vehicles/editar/<int:pk>/", vehicle_views.VehiclesUpdateView.as_view(), name="vehiculo_editar"),
    path("vehicles/eliminar/<int:pk>/", vehicle_views.VehiclesDeleteView.as_view(), name="vehiculo_eliminar"),

    # ORDERS
    path('orders/', OrdersHomeView.as_view(), name='orders'),

    # RECHARGES
    path('recharges/', RechargesHomeView.as_view(), name='recharges'),

    # PAYMENTS
    path('payments/', PaymentsHomeView.as_view(), name='payments'),

    # NOTIFICATIONS
    path('notifications/', NotificationsHomeView.as_view(), name='notifications'),

    # AUTH Para login y logout
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # API REST
    path('api/', include(router.urls)),

]
