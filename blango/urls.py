"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from blango_auth.views import profile
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
from rest_framework.authtoken import views
import blog.views
from django.conf.urls.static import static

# DEBUGGING
# from django.conf import settings
# print(f"Timzone: {settings.TIME_ZONE}")
# DEBUGGING END

## IP GETTING
def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META["REMOTE_ADDR"])


urlpatterns = [
    path('admin/', admin.site.urls),
    path("post-table/", blog.views.post_table, name="blog-post-table"),
    path("", include("blog.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("blog.api.urls")),
    path("api/v1/token-auth/", views.obtain_auth_token),
    path("ip/", get_ip)
]

if settings.DEBUG:
  urlpatterns += [path("__debug__/", include(debug_toolbar.urls))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)