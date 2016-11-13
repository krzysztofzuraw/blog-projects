from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from tasks.views import TaskViewSet
from users.views import ActivateUser, CreateUserView, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', obtain_jwt_token),
    url('^api-register/$', CreateUserView.as_view()),
    url(
        '^api-activate/(?P<token>.+?)/$',
        ActivateUser.as_view(),
        name='activate-user'
    ),
]
