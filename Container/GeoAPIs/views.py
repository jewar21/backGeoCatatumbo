from django.views.decorators.csrf import csrf_protect
from django.views import View
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken

from GeoAPIs.models import UserProductorDb
from GeoAPIs.serializers import UserProductorSerializer, AuthTokenSerializer

# Creación del Token


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

# Vistas para Usuarios Productores


@csrf_protect
@api_view(['GET'])
def user_producer_list(request):
    if request.method == 'GET':
        producers = UserProductorDb.objects.all()
        serializer = UserProductorSerializer(producers, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_protect
@api_view(['GET', 'PUT', 'DELETE'])
def user_producer_detail(request, pk):
    try:
        producer = UserProductorDb.objects.get(pk=pk)
    except UserProductorDb.DoesNotExist:
        return JsonResponse(status=404)

    if request.method == 'GET':
        serializer = UserProductorSerializer(producer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProductorSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        producer.delete()
        return JsonResponse(status=204)
