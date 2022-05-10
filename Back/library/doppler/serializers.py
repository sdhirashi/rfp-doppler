from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    artistid = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Artist
        fields = ['id','name','stagename','nationality','artistid']

class GenreSerializer(serializers.ModelSerializer):
    genreid = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Genre
        fields = ['id','name','genreid']

class AlbumSerializer(serializers.ModelSerializer):
    albumid = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Album
        fields = ['id','name','price','cover','releasedate','stock','albumid']

class SongSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True,read_only=True)
    songid = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Song
        fields = ['id','name','duration','songfile','previewfile','price','songs','songid']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model: Address
        fields = ['id','userid','street','streetnumber','city','postalcode','country']

class OrderSerializer(serializers.ModelSerializer):
    orderid = serializers.StringRelatedField(many=True, read_only = True)
    class Meta:
        model: Order
        fields = ['id','userid','date','orderid']

class OrderSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model: OrderSongs
        fields = ['id','orderid','songid']