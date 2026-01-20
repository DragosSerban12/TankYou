from django.views.generic import TemplateView
from .models import Pago, Reembolso

class PaymentsHomeView(TemplateView):
    template_name = 'payments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagos'] = Pago.objects.all()
        context['reembolsos'] = Reembolso.objects.all()
        return context
