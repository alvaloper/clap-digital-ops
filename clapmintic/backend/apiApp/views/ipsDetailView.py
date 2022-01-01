from rest_framework.views import APIView
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiApp.models.ips import Ips
from apiApp.serializers import IpsSerializer


class IpsDetail(views.APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Ips.objects.get(pk=pk)
        except Ips.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ips = self.get_object(pk)
        serializer = IpsSerializer(ips)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ips = self.get_object(pk)
        serializer = IpsSerializer(ips, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ips = self.get_object(pk)
        ips.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)