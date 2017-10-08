from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .pagination import *
# Create your views here.


class Services(ListView):
    template_name = 'services.html'
    model = ServicesModel
    paginator_class = MyPaginator
    paginate_by = 6

    def get_queryset(self):
        return ServicesModel.objects.order_by('id')

