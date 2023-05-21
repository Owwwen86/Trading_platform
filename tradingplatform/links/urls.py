from django.urls import path

from tradingplatform.links.views import LinkCreateView, LinkListView, LinkView

urlpatterns = [
    # Link API
    path('create', LinkCreateView.as_view(), name='create-link'),
    path('list', LinkListView.as_view(), name='link-list'),
    path('<int:pk>', LinkView.as_view(), name='board'),

]
