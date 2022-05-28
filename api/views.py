from api.models import Material
from api.serializers import MaterialSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MaterialList(APIView):

    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = MaterialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaterialDetail(APIView):

    def get_object(self, id):
        try:
            return Material.objects.get(id=id)

        except Material.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        material = self.get_object(id)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    def put(self, request, id):
        material = self.get_object(id)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        material = self.get_object(id)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)