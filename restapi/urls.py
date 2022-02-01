from django.urls import path

from restapi.views import *

urlpatterns = [
    path('shortlink/detailapi/<int:pk>', ShortlinkDetailApiView.as_view()),
    path('shortlink/createapi',ShortlinkCreateApiView.as_view()),
    path('shortlink/create', ShortlinkCreateView.as_view()),
    path('shortlink/list/', ShortlinkListView.as_view()),
    path('shortlink/detail/<int:pk>', ShortlinkDetailView.as_view()),

]
