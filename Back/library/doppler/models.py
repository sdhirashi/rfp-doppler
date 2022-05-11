from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, null = False)
    stagename = models.CharField(max_length=128, null = False)
    nationality = models.CharField(max_length=128, null = False)
    cover = models.TextField(null=False, default='image')

class Genre(models.Model):
    name = models.CharField(max_length=40, null = False)

class Album(models.Model):
    name = models.CharField(max_length=100, null = False)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, null = False)
    cover = models.TextField(null = False)
    releasedate = models.DateField(null = False)
    stock = models.SmallIntegerField(null = False)
    genreid = models.ForeignKey(Genre, related_name='AlbumGenre', on_delete=models.DO_NOTHING, null = False)

class Song(models.Model):
    name = models.CharField(max_length=100, null = False)
    duration = models.DecimalField(max_digits=4, decimal_places =0, null = False)
    songfile = models.TextField(null = False)
    previewfile = models.TextField(null = False)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, null = False)
    albumid = models.ForeignKey(Album, related_name='SongAlbum', on_delete=models.CASCADE, null = False)
    artistid = models.ForeignKey(Artist, related_name ='SongArtist', on_delete = models.CASCADE, null = False)

class Address(models.Model):
    userid = models.SmallIntegerField(null = False)
    street = models.CharField(max_length=120, null = False)
    streetnumber = models.SmallIntegerField(null = False)
    city = models.CharField(max_length = 40, null = False)
    postalcode = models.SmallIntegerField(null = False)
    country = models.CharField(max_length=40, null = False)

class Order(models.Model):
    userid = models.SmallIntegerField(null = False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    songs = models.ManyToManyField(Song, through='OrderSongs')

class OrderSongs(models.Model):
    orderid = models.ForeignKey(Order, related_name='OrderWithSong', on_delete = models.DO_NOTHING)
    songid = models.ForeignKey(Song, related_name='SongWithOrder', on_delete = models.DO_NOTHING)








