from . import models

from rest_framework import routers, serializers, viewsets


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Thought
        fields = ('recorded_at', 'condition', 'notes')
