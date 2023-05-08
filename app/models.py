from django.db import models


class Truck(models.Model):
    type_truck = models.ForeignKey('TruckModel',
                                   on_delete=models.CASCADE,
                                   verbose_name='Тип грузовика')

    reg_number = models.CharField("Бортовой номер", max_length=100)
    current_load = models.IntegerField("Текущий вес")
    
    class Meta:
        verbose_name_plural = "Грузовики"
        
    def clean(self):
        if self.current_load < 0:
            raise ValueError("Текущий вес не может быть отрицательным")
    
    def validate_unique(self, exclude=None):
        if Truck.objects.filter(
            reg_number=self.reg_number).exclude(id=self.id).exists():
            raise ValueError("Такой бортовой номер уже существует")
    
    @property
    def check_current_load(self):
        max_load = self.type_truck.max_load_capacity
        if self.current_load > max_load:
            percent = ((self.current_load - max_load) / max_load) * 100
            return round(percent, 2)
        else:
            return None
    
    def __str__(self):
        return self.reg_number


class TruckModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Модель", max_length=100)
    max_load_capacity = models.IntegerField("Максимальная грузоподьемность", 
                                            default=0)
    
    class Meta:
        verbose_name_plural = "Модель грузовиков"
        
    def validate_unique(self, exclude=None):
        if TruckModel.objects.filter(name=self.name).exclude(id=self.id).exists():
            raise ValueError("Такая модель уже существует")
    
    def clean(self):
        if self.max_load_capacity < 0:
            raise ValueError(
                "Максимальная грузоподьемность не может быть отрицательной"
                )
    
    def __str__(self):
        return str(self.name)
 
   
