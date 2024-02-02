

from django.urls import path
from . import views
from .views import BranchByDistrictView, YourDistrictView
from django.contrib.auth import views as auth_views


app_name = 'bankapp'

urlpatterns = [

    path('new_page/', views.new_page, name='new_page'),
    path('home/', views.home, name='home'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('branches/', views.branches, name='branches'),
    path('branches/<slug:district_slug>/', BranchByDistrictView.as_view(), name='branches'),
    path('branches/district/<slug:district_slug>/', YourDistrictView.as_view(), name='district'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration_form/', views.registration_form, name='registration_form'),
    path('wikipedia_page/<str:district>/', views.wikipedia_page, name='wikipedia_page'),
    path('get_branches/', views.get_branches, name='get_branches'),

]
