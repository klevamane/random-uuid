
import json
import uuid

from rest_framework import status, generics
from rest_framework.response import Response

from api.models import RandomUid
from api.serializers import RandomUidSerializer


def generate_random_uuid():
    RandomUid(uuid=uuid.uuid4()).save()


class GetUIDView(generics.ListAPIView):
    queryset = RandomUid.objects.all().order_by("-created_at")
    serializer_class = RandomUidSerializer

    def list(self, request, *args, **kwargs):
        generate_random_uuid()
        queryset = self.get_queryset()
        serializer = RandomUidSerializer(queryset, many=True)
        data = json.loads(json.dumps(serializer.data))
        context = {}
        for i in range(len(data)):
            for _, _ in data[i].items():
                context.update({data[i]["created_at"]: data[i]["uuid"]})

        return Response(context, status=status.HTTP_200_OK)
