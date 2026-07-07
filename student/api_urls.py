from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r"students" , api_views.StudentViewSet)

urlpatterns = router.urls