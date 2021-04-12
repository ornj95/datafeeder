"""datafeeder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    error_404,
    error_400,
    error_500,
    error_403,

)
from feeds.views import (
    feeds_home,
)
from .views import (
    home_views,
    delete_item,
    update_item,
    HomeClassView,

)

from api.views import (
    ArticlesViewSet,

)

router_view_set = DefaultRouter()
router_view_set.register('', ArticlesViewSet, basename='item_base')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeClassView.as_view(), name="home"),

    path('crudformHome', home_views, name="crudformhome"),
    path('crudformdelete/<int:id>/', delete_item, name="curdformdelete"),
    path('crudformupdate/<int:id>/', update_item, name="curdformupdate"),

    path('api/', include(router_view_set.urls), name='item_api_view_set'),

    path('feeds_home', feeds_home, name='feeds_home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_change.html'),
         name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]

handler404 = 'account.views.error_404'
handler500 = 'account.views.error_500'
handler403 = 'account.views.error_403'
handler400 = 'account.views.error_400'