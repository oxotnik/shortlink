import random
import string
from datetime import datetime, timedelta

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .forms import ShortLinksForm
from .models import ShortLinks


class ShortLinksView(ListView):
    """Список линков"""
    paginate_by = 3
    model = ShortLinks
    queryset = ShortLinks.objects.all()
    template_name = "shortlinks/shortlinks_list.html"


class AddShortLinkView(View):
    def get(self, request):
        return render(request, "shortlinks/shortlink.html", {})


class AddShortLink(View):
    """ Сократить ссылку """

    @staticmethod
    def generate_short_id():
        """ Генерация случаного кода """
        result = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in
                         range(random.randrange(5, 8)))
        return result

    def get_short_id(self):
        """ Получение случайного года и проверка на наличие в БД """
        is_flag = True
        while is_flag:
            code = self.generate_short_id()
            if not ShortLinks.objects.filter(short_url=code).exists():
                return code

        return None

    def post(self, request):
        form = ShortLinksForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date_create = datetime.today()
            form.date_expiry = datetime.now() + timedelta(days=30)
            short_id = self.get_short_id()  # Тут метод генерации ключа
            form.short_id = short_id
            form.short_url = request.build_absolute_uri('/l/' + short_id)
            form.description = ""
            form.save()
            return redirect("/linkview/" + short_id)
        return render(request, "shortlinks/shortlink.html", {"form": form})


class CreatedShortLink(View):
    """ Сгенерированная ссылка """

    def get(self, request, pk):
        link = ShortLinks.objects.get(short_id=pk)
        return render(request, "shortlinks/shortlinks_view.html", {"link": link})


class ShortLinkRedirect(View):
    """ Редирект ссылки на другой ресурс """

    def get(self, request, pk):
        # shortlink = ShortLinks.objects.get(short_id=pk)

        qs = ShortLinks.objects.filter(short_id=pk).values('url')
        if not qs.exists():
            redirect('/')

        return redirect(qs[0]["url"])


class JsonShortLinkView(View):
    """ Получаем Json одной сокращенной ссылки """

    # def get_queryset(self):
    #     pk = int(self.request.GET.get('link_id'))
    #     queryset = ShortLinks.objects.get(id=pk).values("url", "date_create", "id", "short_url")
    #     return queryset

    def get(self, request, *args, **kwargs):
        link_id = int(self.request.GET.get('link_id'))
        shortlink = ShortLinks.objects.filter(pk=link_id)
        shortlink_json = serializers.serialize("json", shortlink, fields=("url", "short_url", "date_create"))
        return JsonResponse(shortlink_json, safe=False)

        # queryset = list(self.get_queryset())
        # return JsonResponse({"link": queryset}, safe=False)
