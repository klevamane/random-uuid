from rest_framework import serializers

from api.models import RandomUid


class RandomUidSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomUid
        fields = ["uuid", "created_at"]
