from django.conf.urls import url, include
from django.contrib import admin
from products.views import UserCreateView, ProductCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create-user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create-product/$', ProductCreateView.as_view(), name='product_create_view'),
]
