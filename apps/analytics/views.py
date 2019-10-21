import datetime
from rest_framework import viewsets, permissions, mixins, views
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.analytics.models import (
    AnalyticsEvent,
)

from apps.analytics.serializers import (
    AnalyticsEventSerializer,
)


class AnalyticsEventViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = AnalyticsEvent.objects.all()
    serializer_class = AnalyticsEventSerializer

    def get_queryset(self):
        qs = self.queryset
        return qs.order_by("occurred_at")
