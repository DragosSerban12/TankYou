from django.views.generic import TemplateView
from .models import Pedido, Turno

class OrdersHomeView(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedidos'] = Pedido.objects.all()
        context['turnos'] = Turno.objects.all()
        return context