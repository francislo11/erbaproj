# import the 404 as well
from django.shortcuts import get_object_or_404, render
# define Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# load database into view
from .models import Listing
from urllib import response
from django.shortcuts import render, redirect, reverse

# Create your views here.


def blog(request):
    blogs = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {
        'blogs': paged_blogs
    }
    return render(request, 'blogs/blog.html', context)


def qt_01(request):
    return render(request, 'blogs/qt_01.html')


def qt_02(request):
    return render(request, 'blogs/qt_02.html')


def QT(request):
    return render(request, 'blogs/QT.html')


def dt01(request):
    return render(request, 'blogs/dt01.html')


def rm01(request):
    return render(request, 'blogs/rm01.html')

# add additional parameter listing_id route

# get an id or return 404
# def listing(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)
#     context = {
#         'listing': listing
#     }
#     return render(request, 'blogs/blog.html', context)
