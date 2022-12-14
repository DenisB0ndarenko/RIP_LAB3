"""riplab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from riplab3_app import views as quest_hub_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quests', quest_hub_views.QuestViewSet)
router.register(r'genres', quest_hub_views.GenreViewSet)
router.register(r'bookings', quest_hub_views.BookingViewSet)
# router.register(r'bookingsondate', quest_hub_views.AgrBookViewSet)
router.register(r'bookingsondate', quest_hub_views.CountBookingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
