from app.models import StreamPlatform, WatchList
from rest_framework import filters, generics


from app.api import serializers

class StreamPlatformAV(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = serializers.StreamPlatformSerializer


class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = serializers.StreamPlatformSerializer


class WatchListAV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchListSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']


class WatchListDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = serializers.WatchListSerializer