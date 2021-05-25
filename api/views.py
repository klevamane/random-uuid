from rest_framework import response
from rest_framework import status, generics
from rest_framework.response import Response

from api.models import RandomUid
from api.serializers import RandomUidSerializer


def set_true_context(data, msg):
    return {"data": data, "message": msg, "success": True}


class GetUIDView(generics.ListAPIView):
    queryset = RandomUid.objects.all().order_by("-created_at")
    serializer_class = RandomUidSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RandomUidSerializer(queryset, many=True)
        context = set_true_context(serializer.data, "successfull operation")
        return Response(context, status=status.HTTP_200_OK)

