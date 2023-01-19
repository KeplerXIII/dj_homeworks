from django.contrib import admin
from measurement.models import Sensor, Measurement
# Register your models here.

class SensorMeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    inlines = [SensorMeasurementInline]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id','created_at','name',)

    def name(self, obj):
        return obj.sensor.name
