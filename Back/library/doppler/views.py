from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from library.doppler.serializers import *
import base64
from rest_framework.response import Response
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser, JSONParser
from rest_framework import pagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer
    permission_classes = []

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer
    permission_classes = []

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer
    permission_classes = []

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    permission_classes = []

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
    permission_classes = []

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = []

class OrderSongsViewSet(viewsets.ModelViewSet):
    queryset = OrderSongs.objects.all().order_by('id')
    serializer_class = OrderSongsSerializer
    permission_classes = []
