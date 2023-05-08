from typing import Any, Dict
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Truck, TruckModel
from .forms import AddTruckForm, AddTruckModelForm


class IndexView(ListView):
    template_name = 'home.html'
    model = Truck
    context_object_name = 'trucks'

    def get_queryset(self):
        model_id = self.request.GET.get('model', None)
        if model_id:
            queryset = Truck.objects.select_related('type_truck').filter(
                type_truck__id=model_id)
        else:
            queryset = Truck.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        models = TruckModel.objects.all()
        context['models'] = models
        return context


class AddTruckView(CreateView):
    template_name = 'add_truck.html'
    model = Truck
    form_class = AddTruckForm
    success_url = reverse_lazy('start')
    raise_exception = True
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        models = TruckModel.objects.all()
        context['models'] = models
        return context


class AddTruckModelView(CreateView):
    template_name = 'add_models_truck.html'
    model = TruckModel
    form_class = AddTruckModelForm
    success_url = reverse_lazy('start')
    raise_exception = True