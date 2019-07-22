import json
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse

from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm
from .utils import is_json


# Creating, Updating, Deleting, Retrieving (1) -- Update Model

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
        Retrieve, Update, Delete --> Object
    '''
    is_json = True

    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        return qs.first() if qs.count() == 1 else None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        else:
            json_data = obj.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Not allowed, please use the /api/updates/ endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        else:
            if not is_json(request.body):
                error_data = json.dumps({"message": "Invalid data sent, please send using JSON."})
                return self.render_to_response(error_data, status=400)
            else:
                data = json.loads(obj.serialize())
                passed_data = json.loads(request.body)
                data.update(passed_data)
                form = UpdateModelForm(data, instance=obj)
                if form.is_valid():
                    obj = form.save(commit=True)
                    obj_data = json.dumps(data)
                    return self.render_to_response(obj_data, status=201)
                else:
                    if form.errors:
                        data = json.dumps(form.errors)
                        return self.render_to_response(data, status=400)
                    else:
                        json_data = json.dumps({"message": "not valid data"})
                        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        else:
            num_del, item_del = obj.delete()
            if num_del == 1:
                json_data = json.dumps({"message": "successfully deleted."})
                return self.render_to_response(json_data, status=200)
            else:
                json_data = json.dumps({"message": "Counld not delete them, try again later."})
                return self.render_to_response(json_data, status=400)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
        List View
        Create View
    '''
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        if not is_json(request.body):
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        else:
            data = json.loads(request.body)
            form = UpdateModelForm(data)
            if form.is_valid():
                obj = form.save(commit=True)
                obj_data = obj.serialize()
                return self.render_to_response(obj_data, status=201)
            else:
                data = json.dumps(form.errors) if form.errors else {"message": "Not allowed"}
                return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You cannot delete an entire list."})
        return self.render_to_response(data, status=403)



