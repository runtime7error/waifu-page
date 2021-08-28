from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import WaifuSerializer
from core.models import Waifu


class WaifuAPIView(APIView):
    def get(self, request):
        queryset = Waifu.objects.all()

        serializer = WaifuSerializer(queryset, many=True)

        return Response(
            {
                "data": serializer.data,
            },
            status=200,
        )

    def handle_exception(self, exc):
        return super().handle_exception(exc)
