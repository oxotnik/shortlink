from rest_framework import serializers

from shortlink.models import ShortLinks


class ShortlinkDetailSerializer(serializers.ModelSerializer):
    """ Деталь сокращенной ссылки """

    class Meta:
        model = ShortLinks
        fields = '__all__'


class ShortlinksListSerializer(serializers.ModelSerializer):
    """ Деталь сокращенной ссылки """

    class Meta:
        model = ShortLinks
        fields = ('id', 'url', 'date_create', 'short_url')
