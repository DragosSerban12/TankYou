from django.views.generic import TemplateView
from .models import Notificacion

class NotificationsHomeView(TemplateView):
    template_name = 'notifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notificaciones'] = Notificacion.objects.all()
        return context
