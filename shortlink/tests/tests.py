from datetime import datetime

import factory
import pytest
from dateutil.tz import UTC
from factory.fuzzy import FuzzyChoice, FuzzyDateTime, FuzzyText

from shortlink.models import ShortLinks


class ShortLinksFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShortLinks

    url = "https://tresmodo.ru/" + str(FuzzyText())
    description = FuzzyChoice(['description 1', 'description 2', 'description 3'])
    short_id = "XxX"
    short_url = "http://localhost/XxX"
    date_create = FuzzyDateTime(datetime(2008, 1, 1, tzinfo=UTC))


@pytest.fixture
def shortlink(db) -> ShortLinks:
    shortlink = ShortLinksFactory.create()
    return shortlink
    # return ShortLinks.objects.create(url="https://tresmodo.ru/", date_create=datetime.now(), short_id="XxX",
    #                                  short_url="http://localhost/XxX")


def test_filter_shortlink(shortlink):
    assert ShortLinks.objects.filter(short_id="XxX").exists()


def test_url_label(shortlink):
    link = ShortLinks.objects.get(short_id="XxX")
    field_label = link._meta.get_field('url').verbose_name
    assert field_label == 'Ссылка'


def test_first_name_max_length(shortlink):
    link = ShortLinks.objects.get(short_id="XxX")
    max_length = link._meta.get_field('url').max_length
    assert max_length == 255


def test_get_absolute_url(shortlink):
    link = ShortLinks.objects.get(short_id="XxX")
    assert link.get_absolute_url() == "/linkview/XxX/"


""" Views Test """

# def test_view_url_linkslist(shortlink, client):
#     response = client.get('/linkslist')
#     assert response.status_code == 200
