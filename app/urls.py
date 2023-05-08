from django.urls import path
from .views import IndexView, AddTruckView, AddTruckModelView


urlpatterns = [
    path('', IndexView.as_view(), name='start'),
    path('add_truck/', AddTruckView.as_view(), name='add_truck'),
    path('add_models_truck/', AddTruckModelView.as_view(), 
         name='add_models_truck'),
]
