# from django.shortcuts import render

# def main(request):
#     return render(request, 'main/main.html')  # Adjust path if needed


# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm
# from django.contrib.auth import login

# def signup_view(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("/")  
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "signup.html", {"form": form})

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# from django.shortcuts import render

# def main_home(request):
#     return render(request, 'main/main.html')

# # main/views.py
# def home(request):
#     return render(request, 'main/main.html')

# # main/views.py
# from django.shortcuts import render

# def main_view(request):
#     return render(request, 'main/main.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm







# Signup view
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main_home")  # Use named URL
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

# Main view after login
@login_required
def main_home(request):
    return render(request, 'main/main.html')
from django.contrib.auth.decorators import login_required

@login_required
def add_url(request):
    return render(request, 'add/add.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '/main/')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_home')  # <-- manually redirect here
            return redirect(next_url)
    return render(request, 'registration/login.html')
