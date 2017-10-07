from django.shortcuts import render_to_response, get_object_or_404, redirect,HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic.list import ListView
from .forms import CommentForm
from django.core.paginator import Paginator, Page
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


class CommentsPage(ListView):
    model = CommentPost
    template_name = 'comments.html'
    paginator_class = MyPaginator
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        self.form = CommentForm()
        return super(__class__, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(__class__, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        qs = CommentPost.objects.order_by('-id')
        for comment in qs:
           if comment.img_on == False:
               comment.img = '/img/comments/vector-smart-object.png'
        return qs

    def post(self, request, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        if not request.POST.get('honeypot', ''):
            if form.is_valid():
                comment = form.save(commit=False)
                file = form.cleaned_data['img']
                print(file)
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[-1].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                comment.ip_address = ip
                comment.save()
                return HttpResponseRedirect('/comments/')
            else:
                self.object_list = self.get_queryset()
                context =  super(__class__, self).get_context_data(**kwargs)
                context['form'] = form
                return self.render_to_response(context=context)
        else:
            return HttpResponseRedirect('/comments/')

