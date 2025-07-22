# from django.shortcuts import render

# def add_page(request):
#     return render(request, 'add.html')

# from django.shortcuts import render, redirect
# from add.models import URL


# def add_url(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         original_url = request.POST.get('original_url')

#         if title and original_url:
#             new_url = URL(title=title, original_url=original_url)
#             new_url.save()
#             return render(request, 'add/success.html', {'short_url': new_url.short_url})
    
#     return render(request, 'add/add.html')





# import random, string
# from django.shortcuts import render, redirect
# from .models import UrlModel





# from django.contrib.auth import login, authenticate


# def generate_short_code(length=6):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# def add_url(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         original_url = request.POST.get('original_url')
#         short_code = generate_short_code()

#         # Save to DB
#         UrlModel.objects.create(title=title, original_url=original_url, short_url=short_code)

#         return redirect('main')  # or show success message

#     return render(request, 'add/add.html')







# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import UrlModel
# from .forms import UrlModelForm 
#  # assume you have a form

# @login_required
# def create_url(request):
#     user = request.user
#     url_count = UrlModel.objects.filter(user=user).count()

#     if url_count >= 5:
#         messages.error(request, "You can only add up to 5 URLs.")
#         return redirect('your-url-list-or-home-view-name')  # change accordingly

#     if request.method == 'POST':
#         form = UrlModelForm(request.POST)
#         if form.is_valid():
#             url = form.save(commit=False)
#             url.user = user
#             url.save()
#             messages.success(request, "URL added successfully!")
#             return redirect('your-url-list-or-home-view-name')
#     else:
#         form = UrlModelForm()

#     return render(request, 'your-template.html', {'form': form})



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import UrlModel
# from .forms import UrlModelForm



# @login_required
# def create_url(request):
#     user = request.user
#     url_count = UrlModel.objects.filter(user=user).count()

#     if url_count >= 5:
#         messages.error(request, "You can only add up to 5 URLs.")
#         return redirect('create-url')  # or any other view name

#     if request.method == 'POST':
#         form = UrlModelForm(request.POST)
#         if form.is_valid():
#             url = form.save(commit=False)
#             url.user = user
#             url.save()
#             messages.success(request, "URL added successfully!")
#             return redirect('create-url')
#     else:
#         form = UrlModelForm()

#     return render(request, 'your-template.html', {'form': form})





# from django.shortcuts import render, redirect
# from .models import UrlModel
# from django.contrib.auth.decorators import login_required
# import random, string

# def generate_short_code(length=6):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# @login_required
# def add_url(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         original_url = request.POST.get('original_url')
#         short_code = generate_short_code()

#         # Check URL count
#         user = request.user
#         if UrlModel.objects.filter(user=user).count() >= 5:
#             return render(request, 'add/error.html', {'error': "Limit reached."})

#         UrlModel.objects.create(user=user, title=title, original_url=original_url, short_url=short_code)
#         return redirect('main')  # Update this to the right redirect view

#     return render(request, 'add/add.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import UrlModel
from .forms import UrlForm  # make sure this form is defined
import random, string




def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@login_required
def add_url(request):
    user = request.user

    if UrlModel.objects.filter(user=user).count() >= 5:
        return render(request, 'add/error.html', {'error': "You have reached the maximum limit of 5 URLs."})

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = user
            url.short_url = generate_short_code()
            url.save()
            return redirect('main_home')    # update this to your correct redirect
    else:
        form = UrlForm()

    return render(request, 'add/add.html', {'form': form})


# add/views.py

# add/views.py

# from django.shortcuts import render
# from .models import UrlModel

# def url_list_view(request):
#     urls = UrlModel.objects.all().order_by('-id')
#     return render(request, 'add/url_list.html', {'urls': urls})  # Include app folder if template is under add/templates/add/


# from django.core.paginator import Paginator
# from django.shortcuts import render
# from .models import UrlModel

# def url_list_view(request):
#     url_list = UrlModel.objects.all().order_by('-id')
#     paginator = Paginator(url_list, 5)  # Show 5 URLs per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'url_list.html', {'page_obj': page_obj})



# from django.db.models import Q  # For complex queries
# from .models import UrlModel
# from django.shortcuts import render

# def url_list_view(request):
#     query = request.GET.get('q')  # Get search term from query param
#     if query:
#         urls = UrlModel.objects.filter(
#             Q(title__icontains=query) | Q(url__icontains=query)
#         ).order_by('-id')
#     else:
#         urls = UrlModel.objects.all().order_by('-id')
#     return render(request, 'url_list.html', {'urls': urls, 'query': query})


# from django.shortcuts import render
# from django.core.paginator import Paginator
# from django.db.models import Q
# from .models import UrlModel

# def url_list_view(request):
#     query = request.GET.get('q')  # Search term
#     url_list = UrlModel.objects.all().order_by('-id')

#     if query:
#         url_list = url_list.filter(
#             Q(title__icontains=query) | Q(url__icontains=query)
#         )

#     paginator = Paginator(url_list, 5)  # Show 5 URLs per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'add/url_list.html', {
#         'page_obj': page_obj,
#         'query': query
#     })

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import UrlModel


@login_required
def url_list_view(request):
    query = request.GET.get('q')  # Search input
    url_list = UrlModel.objects.all().order_by('-id')

    if query:
        url_list = url_list.filter(
            Q(title__icontains=query) | Q(original_url__icontains=query) | Q(short_url__icontains=query)
        )

    paginator = Paginator(url_list, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'add/url_list.html', {
        'page_obj': page_obj,
        'query': query,
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import UrlModel
from .forms import UrlForm
from django.contrib import messages
from django.core.paginator import Paginator


# Edit View
def url_edit_view(request, pk):
    url_instance = get_object_or_404(UrlModel, pk=pk)
    if request.method == 'POST':
        form = UrlForm(request.POST, instance=url_instance)
        if form.is_valid():
            form.save()
            return redirect('url_list')
    else:
        form = UrlForm(instance=url_instance)
    return render(request, 'add/url_edit.html', {'form': form})

# Delete View
def url_delete_view(request, pk):
    url_instance = get_object_or_404(UrlModel, pk=pk)
    if request.method == 'POST':
        url_instance.delete()
        return redirect('url_list')
    return render(request, 'add/url_confirm_delete.html', {'url': url_instance})





