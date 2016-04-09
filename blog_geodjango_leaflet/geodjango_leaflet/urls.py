from django.conf.urls import include, url
from django.contrib import admin
from voivodeships.views import points_view, voivodeships_view, MainPageView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^points.data/', points_view, name='points'),
    url(r'^voivodeships.data/', voivodeships_view, name='voivodeships'),
    url(r'^$', MainPageView.as_view()),
]
