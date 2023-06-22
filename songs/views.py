from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Song
from .serializers import SongSerializer


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get(self.lookup_field))

    def perform_create(self, serializer):
        serializer.save(album_id=self.kwargs.get(self.lookup_field))
