from django.conf.urls import url, include
from django.contrib import admin
from tasks.views import TaskViewSet
from users.views import UserViewSet, CreateUserView, ActivateUser
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


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
