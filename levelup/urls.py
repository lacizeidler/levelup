from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import GameTypeView
from levelupapi.views.event import EventView
from levelupapi.views.game import GameView
from levelupapi.views.gamer import GamerView

# This router is similar to SimpleRouter as above, but additionally includes a default API root view, that returns a response containing hyperlinks to all the list views. It also generates routes for optional . json style format suffixes.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'gamers', GamerView, 'gamer')
router.register(r'events', EventView, 'event')
# Third parameter is for error control. 

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

