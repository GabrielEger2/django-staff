from django.views.generic import CreateView
from .models import Document

class DocumentCreate(CreateView):
    model = Document
    fields = ['name', 'file']

    def form_valid(self, form):
        form.instance.holder_id = self.kwargs['employee_id']
        return super().form_valid(form)
        