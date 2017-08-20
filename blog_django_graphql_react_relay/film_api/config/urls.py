from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from graphene_django.views import GraphQLView

from film_database.actors import views as actors_views
from film_database.films import views as films_views
from config.schema import schema

router = routers.DefaultRouter()
router.register(r'actors', actors_views.ActorsViewSet)
router.register(r'films', films_views.FilmsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
