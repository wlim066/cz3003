from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'dengues', views.dengueViewsetManager)
router.register(r'hazes', views.hazeViewsetManager)
router.register(r'alls', views.allViewsetManager)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]