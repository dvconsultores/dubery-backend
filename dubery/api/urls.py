
# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from . import views

# define the router
router = routers.DefaultRouter()


# define the router path and viewset to be used
router.register(r'lentes', views.lentesViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
]    
