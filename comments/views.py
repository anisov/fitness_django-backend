from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from comments.models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from .forms import CommentForm
from django.core.paginator import Paginator, Page
from django.views.decorators.csrf import ensure_csrf_cookie

from django.views.generic.base import TemplateView
# Create your views here.
class MyPage(Page):
    def range_before(self):
        i = self.number - 2
        if i <= 0:
            i = 1
        return range(i, self.number)

    def range_after(self):
        b = self.number + 1
        e = b + 2
        if e > self.paginator.num_pages:
            e = self.paginator.num_pages + 1
        return range(b, e)


class MyPaginator(Paginator):
    def _get_page(self, *args, **kwargs):
        return MyPage(*args, **kwargs)


class Comments_page(ListView):
    model = Comment_post
    template_name = 'comments.html'
    paginator_class = MyPaginator
    paginate_by = 1

