from django.urls import path
from measurement.views import test

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('test/', test)
]
