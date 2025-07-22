# url/urls.py (project-level urls.py)

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),  # your main app
#     path('add/', include('add.urls')),  # your add app
# ]



from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('main/', include('main.urls')),      # main app
#     path('add/', include('add.urls')),
    
       
       
       
       
       
       
#          # add app
#  path('accounts/', include('django.contrib.auth.urls')), 

# ]
# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),  # root URL points to main app
#     path('add/', include('add.urls')),  # add app
#     path('accounts/', include('django.contrib.auth.urls')),  # login/logout
#       path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]


# from django.urls import path, include
# from main import views as main_views
# from django.contrib.auth import views as auth_views




# urlpatterns = [
#     path('', main_views.main_home, name='home'),  # Set this as the default page
#     path('', include('main.urls')),
#     path('add/', include('add.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),  # for login/logout
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]



# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from main import views as main_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     # Default home page
#     path('', main_views.main_home, name='home'),

#     # Include app URLs
#     path('main/', include('main.urls')),
#     path('add/', include('add.urls')),

#     # Auth views (login/logout)
#     path('accounts/', include('django.contrib.auth.urls')),  # Handles /login/ and /logout/
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]


# from django.contrib.auth import views as auth_views
# from django.urls import path, include
# from main import views as main_views

# urlpatterns = [
#     path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Show login first
#     path('main/', main_views.main_home, name='main_page'),  # After login, go here
#     path('add/', include('add.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),  # for login/logout/password
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from main import views as main_views
# from add import views as add_views


# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('main.urls')),  # root URL points to main app
# #     path('add/', include('add.urls')),  # add app
# #     path('accounts/', include('django.contrib.auth.urls')),  # login/logout
# #       path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# # ]

# urlpatterns = [
#     path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('main/', main_views.main_home, name='main_page'),
#     #path('signup/', signup_view, name='signup'),  # if you have signup
#     path('add/', include('add.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]




from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views  # assuming your app is called `main`

# urlpatterns = [
#     path('admin/', admin.site.urls),
#      path('', include('main.urls')), 
#     path('add/', include('add.urls')),  
#     path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # default route
#     path('main/', main_views.main_home, name='main_home'),
#     path('add/', main_views.add_url, name='add_url'),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('signup/', main_views.signup, name='signup'),  # this must match your `views.signup`
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from main import views as main_views  # your views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Authentication
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
#     path('signup/', main_views.signup, name='signup'),

#     # Main and Add apps
#     path('main/', include('main.urls')),   # all views like main_home should be routed inside main/urls.py
#     path('add/', include('add.urls')),     # views like url_list_view or add_url

#     # Optional: redirect base URL to login
#     path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='root_login'),
# ]


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from main import views as main_views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     path('login/', auth_views.LoginView.as_view(), name='login'),  # ✅ Login
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
#     path('', main_views.main_home, name='main_home'),  # ✅ home after login
#     path('signup/', main_views.signup, name='signup'),

#     path('add/', include('add.urls')),
#     path('main/', include('main.urls')),  # assumes main/urls.py exists
# ]


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
      path('accounts/', include('django.contrib.auth.urls')), 
    
    # Login / logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Sign up
    path('signup/', main_views.signup, name='signup'),

    # Main app views
    path('main/', main_views.main_home, name='main_home'),

    # Include app routes
    path('main/', include('main.urls')),
    path('add/', include('add.urls')),
  path('', lambda request: redirect('login/', permanent=False)),


]
