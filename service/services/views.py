from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    # queryset = Subscription.objects.all().select_related('client', 'plan', 'client__user').only(
    #     "id", "plan_id",
    #     "client__company_name", "client__user__email", 'plan__plan_type')
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user') \
                                                    .only('company_name',
                                                          'user__email'))
    )
    serializer_class = SubscriptionSerializer

