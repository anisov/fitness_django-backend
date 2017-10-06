from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect,HttpResponseRedirect
from comments.models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from .forms import CommentForm
from django.core.paginator import Paginator, Page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.detail import SingleObjectMixin
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


class CommentsPage(TemplateView):
    #ListView need change
    model = CommentPost
    queryset = CommentPost.objects.order_by('id')
    template_name = 'comments.html'
    paginator_class = MyPaginator
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        self.form = CommentForm()
        return super(CommentsPage, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentsPage, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['object_list'] = self.queryset
        return context

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if not request.POST.get('honeypot', ''):
            if form.is_valid():
                print(3)
                comment = form.save(commit=False)
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[-1].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                comment.ip_address = ip
                comment.save()
                return HttpResponseRedirect('/comments/')
            else:
                context = super(CommentsPage, self).get_context_data(**kwargs)
                context['form'] = form
                return self.render_to_response(context=context)
        else:
            return HttpResponseRedirect('/comments/')

