from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Vehiculo


class VehiclesCreateView(LoginRequiredMixin, CreateView):
    model = Vehiculo
    fields = ['matricula', 'marca', 'modelo', 'anyo_compra', 'color', 'tipo_combustible']
    template_name = 'vehicles/Vehiculo_form.html'
    success_url = reverse_lazy('vehicles')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class VehiclesUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehiculo
    fields = ['matricula', 'marca', 'modelo', 'anyo_compra', 'color', 'tipo_combustible']
    success_url = reverse_lazy('vehicles')
    login_url = 'login'


class VehiclesDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehicles')
    login_url = 'login'


class VehiclesHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'vehicles.html'
    paginate_by = 2
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        marca = self.request.GET.get('marca')
        anio = self.request.GET.get('anio')
        ordenar_marca = self.request.GET.get('ordenar_marca')
        ordenar_anio = self.request.GET.get('ordenar_anio')
        page = self.request.GET.get('page')

        vehiculos = Vehiculo.objects.filter(usuario=self.request.user)

        # FILTROS
        if marca:
            vehiculos = vehiculos.filter(marca__icontains=marca)

        if anio and anio.isdigit():
            vehiculos = vehiculos.filter(anyo_compra=anio)

        # ORDENACIÓN
        ordenaciones = []

        if ordenar_marca == "True":
            ordenaciones.append("-marca")

        if ordenar_anio == "True":
            ordenaciones.append("anyo_compra")

        if ordenaciones:
            vehiculos = vehiculos.order_by(*ordenaciones)

        # PAGINACIÓN
        paginator = Paginator(vehiculos, self.paginate_by)
        page_obj = paginator.get_page(page)

        # CONTEXTO
        context["vehiculos"] = page_obj
        context["page_obj"] = page_obj
        context["marca"] = marca
        context["anio"] = anio
        context["ordenar_marca"] = ordenar_marca
        context["ordenar_anio"] = ordenar_anio

        return context
