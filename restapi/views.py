from django.http import Http404
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from shortlink.models import ShortLinks
from .serializers import ShortlinkDetailSerializer, ShortlinksListSerializer


class ShortlinkCreateApiView(APIView):
    """ Создать короткую ссылку """

    def post(self, request):
        serializer = ShortlinkDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def post(self, request):
    serializer = ShortlinkDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortlinkDetailApiView(APIView):
    """ Одна короткая ссылка """

    def get_object(self, pk):
        try:
            return ShortLinks.objects.get(pk=pk)
        except ShortLinks.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        link = ShortLinks.objects.get(id=pk)
        serializer = ShortlinkDetailSerializer(link)
        return Response(serializer.data)

    def put(self, request, pk):
        link = self.get_object(pk)
        serializer = ShortlinkDetailSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        link = self.get_object(pk)
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShortlinkCreateView(generics.CreateAPIView):
    """ Создать короткую ссылку """
    serializer_class = ShortlinkDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)


@permission_classes([IsAuthenticated])
class ShortlinkListView(generics.ListAPIView):
    """ Список все линков """
    serializer_class = ShortlinksListSerializer
    queryset = ShortLinks.objects.all()


class ShortlinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Получение данные об одном линке """
    serializer_class = ShortlinkDetailSerializer
    queryset = ShortLinks.objects.all()
    permission_classes = (IsAuthenticated,)
