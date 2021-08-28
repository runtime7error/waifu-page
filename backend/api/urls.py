from django.urls import include, path
from api.views import WaifuAPIView

urlpatterns = [
    path('waifu/', WaifuAPIView.as_view()),
]
