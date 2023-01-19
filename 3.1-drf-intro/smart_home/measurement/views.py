# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from measurement.models import Measurement, Sensor

@api_view(['GET'])
def test(request):
    data = {'x': 'y'}
    return Response(data)

