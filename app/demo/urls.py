"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles

from material.admin.sites import site

site.site_header = _('Demo')
site.site_title = _('Demo')
site.favicon = staticfiles('demo.png')
site.main_bg_color = 'green'
site.main_hover_color = 'yellow'
site.profile_picture = staticfiles('profile-background.jpeg')
site.profile_bg = staticfiles('profile-background.jpeg')
site.login_logo = staticfiles('profile-background.jpeg')
site.logout_bg = staticfiles('profile-background.jpeg')
site.show_themes = True


urlpatterns = i18n_patterns(
    path('admin/', include('material.admin.urls')),
    path('', RedirectView.as_view(url='admin/', permanent=False), name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
