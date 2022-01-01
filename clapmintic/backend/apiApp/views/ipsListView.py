
from rest_framework.views import APIView
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiApp.models.ips import Ips
from apiApp.serializers import IpsSerializer

class IpsList(views.APIView):

    #@api_view(['POST'])
    #def pruebaluisjose(request):
    #    datos = request.data 
    #    id_reps = datos["id_reps"]
    #    nombre = datos["nombre"]

    #    print(id_reps)
    #    print(nombre)
    #    ip = Ips(id_reps='6', nombre='ips cuartaa' , tipo_de_entidad='privada', representante='persona', nivel_de_atencion='basico')
    #    ip.save()

    #   return Response({"Prueba":"Prueba con Luisjose"})

    def get(self, request, format=None):
        ips = Ips.objects.all()
        serializer = IpsSerializer(ips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IpsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET'])
#def pruebaandres(request):
#    if request.method == 'GET':
#        ips = Ips.objects.all()
#        ips_serializer=IpsSerializer(ips,many=True)
#        return Response({"Paso.."}, ips_serializer.data)
    
    
    #http_method_names = ['get', 'head']

    #ips = Ips.objects.all()
    #ips_serializer=IpsSerializer(ips,many=True)
    
    #datos = request.data
    
    #id_reps = datos["id_reps"]
    #nombre = datos["nombre"]

    #print(id_reps)
    #print(nombre)
    
    #ip = Ips(id_reps='6', nombre='ips cuartaa' , tipo_de_entidad='privada', representante='persona', nivel_de_atencion='basico')
    
    #ip = Ips.objects.all()
    
    #print(ip)
    
    #ip.getAll()

    #return Response({"Prueba":"Prueba con Luisjose"})
    #return Response(ips_serializer.data,status=status.HTTP_200_OK)