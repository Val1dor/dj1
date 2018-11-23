# tutorial/tables.py
import django_tables2 as tables
from .models import Sensor

class SensorTable(tables.Table):
    class Meta:
        model = Sensor
        template_name = 'django_tables2/bootstrap.html'