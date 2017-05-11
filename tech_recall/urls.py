from django.conf.urls import url, include
from django.contrib import admin
from products.views import UserCreateView, ProductCreateView, AccountDetailView, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create-user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^create-product/$', ProductCreateView.as_view(), name='product_create_view'),
    url(r'^account/(?P<pk>\d+)/$', AccountDetailView.as_view(), name='account_detail_view'),
    url(r'^passthru/$', home, name='passthru_view')
]
