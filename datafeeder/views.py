from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from .forms import ItemCreation
from account.models import Articles
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

# Funciton for showing all items in menu and adding new items
def home_views(request):
    if request.POST:
        form = ItemCreation(request.POST)

        if form.is_valid():

            # Using Model Class Object
            cond = False
            if cond:
                name = form.cleaned_data['heading']
                body = form.cleaned_data['body']
                category = form.cleaned_data['category']
                content_type = form.cleaned_data['content_type']
                source_link = form.cleaned_data['source_link']
                image_link = form.cleaned_data['image_link']
                tags = form.cleaned_data['tags']
                author = form.cleaned_data['author']
                published_date = form.cleaned_data['published_date']
                published_time = form.cleaned_data['published_time']

                obj = Articles(name=name, body=body, category=category, content_type=content_type,
                                     source_link=source_link, image_link=image_link)
                obj.save()

            # Using Django Form
            else:
                form.save()
            form = ItemCreation()
    else:
        form = ItemCreation()

    items = Articles.objects.all()
    # Paginator
    p = Paginator(items, 5)

    page_num = request.GET.get('page', 1)

    print("Number of Pages")
    print(p.num_pages)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'crud_django_form/Home.html', {'form': form, 'items': page})


# This function will delete an item from the menu
@permission_required('admin.can_add_log_entry', login_url='login')
def delete_item(request, id):
    if request.POST:
        item = Articles.objects.get(pk=id)
        item.delete()
        return redirect('crudformhome')


# This function will edit an item from the menu
def update_item(request, id):
    if request.POST:
        item = Articles.objects.get(pk=id)
        itemform = ItemCreation(request.POST, instance=item)
        if itemform.is_valid():
            itemform.save()
        return redirect('crudformhome')
    else:
        item = Articles.objects.get(pk=id)
        itemform = ItemCreation(instance=item)
    return render(request, 'crud_django_form/updateitem.html', {'form': itemform})


@method_decorator(login_required(redirect_field_name=''), name='dispatch')
class HomeClassView(View):
    def get(self, request):
        return render(request,'Home.html')
