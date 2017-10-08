from django.core.paginator import Paginator, Page


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