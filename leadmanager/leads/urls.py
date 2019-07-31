from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()

router.register('api/leads', LeadViewSet, 'lead')

urlpatterns = router.urls