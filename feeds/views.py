from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

# Create your views here.
from feeds.models import Feeds


@login_required(redirect_field_name='')
def feeds_home(request):
    # items = Feeds.objects.all().filter(published__date=datetime.today())
    # items_ordered = items.order_by('-published')
    # items = items_ordered
    items = Feeds.objects.all().order_by('-published')[:1000]

    # Paginator
    p = Paginator(items, 50)

    page_num = request.GET.get('page', 1)

    print("Number of Pages")
    print(p.num_pages)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'feeds/feed_home.html', {'items': page})
