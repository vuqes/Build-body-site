from .models import *


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Add.objects.all()
        context['cats'] = cats
        return context

