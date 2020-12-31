from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room,Image
from .serializers import RoomSerializer



#/api/room/list?nw_lat=52.922518903189086&nw_lng=-1.5258722939453264&se_lat=52.350813267104314&se_lng=-0.7444697060547014
@api_view(['GET', ])
def api_room_list_view(request,*args,**kwargs):
    nw_lat = request.query_params.get('nw_lat', 0)
    nw_lng = request.query_params.get('nw_lng', 0)
    se_lat = request.query_params.get('se_lat', 0)
    se_lng = request.query_params.get('se_lng', 0)
    try:
        rooms = Room.objects.all().filter(latitude__lte=nw_lat).filter(latitude__gte=se_lat).filter(longitude__gte=nw_lng).filter(longitude__lte=se_lng)
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RoomSerializer(rooms,many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def api_room_all_view(request,*args,**kwargs):
    try:
        
        rooms = Room.objects.all()
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RoomSerializer(rooms,many=True)
        return Response(serializer.data)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer
