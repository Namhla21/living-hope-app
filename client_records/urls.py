from django.urls import path
from .views import home, hct_page, lse_page, register_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('hct/', hct_page, name='hct_page'),
    path('lse/', lse_page, name='lse_page'),
]