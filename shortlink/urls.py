from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", views.AddShortLinkView.as_view()),
    path('linkview/<str:pk>/', views.CreatedShortLink.as_view(), name='view_link'),
    path("linkslist", login_required(views.ShortLinksView.as_view())),
    path("add_link/", views.AddShortLink.as_view(), name="add_link"),
    path("l/<str:pk>/", views.ShortLinkRedirect.as_view(), name="redirect_link"),
    path("getonelink/", views.JsonShortLinkView.as_view(), name="getonelink")
]
