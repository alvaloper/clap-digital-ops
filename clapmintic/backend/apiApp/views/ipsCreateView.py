from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apiApp.serializers.userSerializer import UserSerializer
from apiApp.serializers.ipsSerializer import IpsSerializer


class IpsCreateView(views.APIView):
    
    #def post(self, request, *args, **kwargs):
    #    serializer = IpsSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save()

    #    tokenData = {
    #        "username": request.data["username"], "password": request.data["password"]}
    #    tokenSerializer = TokenObtainPairSerializer(data=tokenData)
    #    tokenSerializer.is_valid(raise_exception=True)

    #    return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = IpsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)