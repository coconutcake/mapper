from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.http import QueryDict
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
import map.models
import room_equipment.models
import stock.models
# Create your views here.
import map.forms
from func import functions as fnc





class AreaView(View):

    """
    Map
    """

    template_name = "map/area.html"

    def get(self, request, *args, **kwargs):

        return render(
            request, 
            self.template_name, 
            self.get_context(request, *args, **kwargs)
            )
    

    def get_context(self, request, *args, **kwargs):


        area_pk = self.request.GET.get('pk')
        area = map.models.Area.objects.get(pk=area_pk)
        area_fields = map.models.Field.objects.filter(area_fk_id=area_pk)

        rows = list(map.models.Field.objects.filter(area_fk_id=area_pk).values_list('x', flat=True).distinct())
        columns = list(map.models.Field.objects.filter(area_fk_id=area_pk).values_list('y', flat=True).distinct())

        matrix = []

        for row in rows:
            dirow = {}
            dirow['row'] = row
            dirow['columns'] = []
            for column in columns:
                dico = {}
                dico['x'] = row
                dico['y'] = column
                dico['field'] = None
                for field in area_fields:
                    if field.x == dico['x'] and field.y == dico['y']:
                        dico['field'] = field
                dirow['columns'].append(dico)
            matrix.append(dirow)



        context = {
            "get_area_fields": area_fields,
            "rows":rows,
            "columns": columns,
            "matrix": matrix,
            "area": area
        }

        print(area_fields)

        return context





class FieldDetailView(View):
    """ 
    
    """
    template_detail_form = "map/forms/field_detail_form.html"
    detail_form = map.forms.FieldDetailForm
    model = map.models.Field

    def get_context_data(self,**kwargs):

        context = {
            "detail_form": self.detail_form,
        }
        return context

    def get(self, request, pk=None, *args, **kwargs):

        context = self.get_context_data()
        field_pk = self.request.GET.get('pk')
        field_instance = map.models.Field.objects.get(pk=field_pk)
        container = field_instance.container_fk if field_instance.container_fk else []
        fields_of_container = map.models.Field.objects.filter(container_fk=container) if container else [field_instance]
        form_instances = []

        for instance in fields_of_container:
            form_instances.append(self.detail_form(instance=instance))

        if request.method == "GET":
            if field_pk:
                return render(
                    request,
                    self.template_detail_form,
                    {
                        "detail_form":self.detail_form(instance=field_instance),
                        "detail_forms":form_instances
                    }
                )
        
        return render(
            request,
            self.template_detail_form,
            {
                "detail_form":self.detail_form(instance=field_instance),
                "detail_forms":form_instances
            }
        )

    def prepare_form_data(self,request,data_key=None,*args,**kwargs):

        data = request.POST

        for k,v in data.items():
            if k == data_key:
                data2 = json.loads(json.dumps(data.get(data_key, '')))

                return QueryDict(data2)

    def get_object(self, *args, **kwargs):

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

    def post(self, request, *args,**kwargs):

        form_data = self.prepare_form_data(
            request,
            data_key="data", #< - {"data": JSON.Stringify($data)}
            )

        instance = self.model.objects.get(pk=self.request.GET.get('pk'))
        form = self.detail_form(data=form_data,instance=instance)

        if form.is_valid():
            form.save()
            return JsonResponse(data={"status":"OK"})
        else:
            return JsonResponse(data={"status":"Failed"})
