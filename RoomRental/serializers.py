from rest_framework import serializers
from .models import Room,Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('room','image')

class RoomSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True)
    #images = serializers.PrimaryKeyRelatedField(many=True,queryset = )
    class Meta:
        model = Room
        fields = ('id','title','price','latitude','longitude','images')