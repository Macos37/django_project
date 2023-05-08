from typing import Any, Dict
from django.forms import ModelForm
from .models import Truck, TruckModel


class AddTruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'

      
class AddTruckModelForm(ModelForm):
    class Meta:
        model = TruckModel
        fields = '__all__'
        