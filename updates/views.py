from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from cfeapi.mixins import JsonResponseMixin
from .models import Update

data = {
        "count": 1000,
        "content": "some new content"
}


def json_example_view(request):
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        return self.render_to_json_response(data)


class SerializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        #data = serialize('json', [obj,], fields=('user', 'content'))
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')


class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        #data = serialize('json', qs, fields=('user', 'content'))
        data = qs.serialize()
        return HttpResponse(data, content_type='application/json')
