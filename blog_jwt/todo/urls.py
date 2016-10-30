from django.conf.urls import url, include
from django.contrib import admin
from tasks import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', obtain_jwt_token),
]
