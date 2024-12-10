from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

class HotelListAPIView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

class RoomListAPIView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
class HotelDetailAPIView(APIView):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    
class RoomDetailAPIView(APIView):
    def get(self, request, room_id):
        try:
            room = Room.objects.get(id=room_id)
            serializer = RoomSerializer(room)
            return Response(serializer.data, status=200)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=404)