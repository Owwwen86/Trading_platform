from rest_framework import generics

from tradingplatform.links.models import Link
from tradingplatform.links.serializer import LinkCreateSerializer, LinkSerializer
from tradingplatform.links.permissions import UserLinkPermissions


class LinkCreateView(generics.CreateAPIView):
    serializer_class = LinkCreateSerializer
    permission_classes = [UserLinkPermissions]


class LinkListView(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [UserLinkPermissions]

    def get_queryset(self):
        queryset = Link.objects.all()
        country = self.request.query_params.get('country')
        if country:
            queryset = Link.objects.filter(contacts__Country=country)
        return queryset


class LinkView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UserLinkPermissions]
    serializer_class = LinkSerializer

    def get_queryset(self):
        return Link.objects.all()
