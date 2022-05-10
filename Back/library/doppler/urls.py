from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'artist',views.ArtistViewSet)
router.register(r'genre',views.GenreViewSet)
router.register(r'album',views.AlbumViewSet)
router.register(r'song',views.SongViewSet)
router.register(r'address',views.AddressViewSet)
router.register(r'order',views.OrderViewSet)
router.register(r'ordersongs',views.OrderSongsViewSet)

urlpatterns = [
	#path('thing', views.ThingView.as_view()),
	path('', include(router.urls)),
]