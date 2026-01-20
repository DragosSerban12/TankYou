from datetime import date, timedelta
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from .forms import UsuarioForm, UsuarioUpdateForm
from .models import Usuario
from vehicles.models import Vehiculo
from orders.models import Pedido
from payments.models import Pago
from recharges.models import Recarga
from notifications.models import Notificacion


# CRUDs
class UserCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect(self.success_url)


class ProyectoUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        user = form.save(commit=False)

        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)

        user.save()
        return redirect(self.success_url)


class ProyectoDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('Home')


# Paginacion de Usuarios
class UsersListView(ListView):
    model = Usuario
    template_name = "users.html"
    paginate_by = 5
    context_object_name = "usuarios"


# Pagina de Usuarios
class UsersHomeView(TemplateView):
    template_name = 'users.html'


# HOME VIEW
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        letras = self.request.GET.get('letras')
        
        # FILTROS
        if letras:
            context['usuarios'] = Usuario.objects.filter(nombre__icontains=letras)
        else:
            context['usuarios'] = Usuario.objects.all()
            marcado_vista = self.request.GET.get('marcado')
            if marcado_vista == 'True':
                context['usuarios'] = context['usuarios'].order_by('nombre')
            context['marcado'] = marcado_vista
       
        # Esto lo que realmente hace es obtener todos los objetos de las otras aplicaciones
        context['vehiculos'] = Vehiculo.objects.all()
        context['pedidos'] = Pedido.objects.all()
        context['pagos'] = Pago.objects.all()
        context['recargas'] = Recarga.objects.all()
        context['notificaciones'] = Notificacion.objects.all()

        return context
