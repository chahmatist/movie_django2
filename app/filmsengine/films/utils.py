from django.shortcuts import render
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

class PaginatorMixin(object):
    def __init__(self, queryset, item_pages, request_page):
        self.queryset = queryset          #egg: models.Post.objects.all()
        self.item_pages = item_pages        #egg: int 10 `is number per page`
        self.request_page = request_page      #egg: request.GET.get('page')

    def queryset_paginated(self):
        paginator = Paginator(self.queryset, self.item_pages)
        page_number = self.request_page
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
            'page_object': page,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginated': is_paginated
        }
        return context