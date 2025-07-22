# # blog/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='main'),
# ]


# # main/urls.py
# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from add import views as add_views


# urlpatterns = [
#      path('', views.home, name='main_page'),
#     # path('', views.main, name='main'),
#      path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     # path("", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
#     path("signup/", views.signup_view, name="signup"),
#      #path('', views.main_home, name='main_home'),
#     #  path("login/", auth_views.LoginView.as_view(), name='login'),
#     #path('', views.main_view, name='main_page'),
#      path('main/', views.main_page, name='main_page'),

#     #path('', views.main_view, name='main_page'),
# ]





# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
#     path('main/', views.main_home, name='main_page'),  # go here after login
#     path('signup/', views.signup_view, name='signup'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
# ]


# # in your url/urls.py or wherever your main urls.py is

# from django.contrib import admin
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import CustomLoginView
# from main import views  # replace with your actual app name

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', auth_views.LoginView.as_view(), name='login'),
#     path('signup/', views.signup_view, name='signup'),  # ✅ this must exist
#     path('main/', views.main_page, name='main_page'),
#     path('add/', views.add_url, name='add_url'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
#     # path('login/', CustomLoginView.as_view(), name='login')
# ]


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from add.views import url_list_view 
from add.views import add_url

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', views.main_home, name='main_home'),
    #  path('add/',add_url, name='add_url'),
    path('add/',url_list_view, name='url_list'),
   

    path('signup/', views.signup, name='signup'),
]
