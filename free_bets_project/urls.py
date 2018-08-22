"""free_bets_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views

from bets import urls as bets_urls, views as bets_views
from market import urls as market_urls
from accounts import urls as accounts_urls
from betting_tools import urls as tools_urls

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap as wagtail_sitemap

from wagtailimportexport import urls as wagtailimportexport_urls

urlpatterns = [
    path('', bets_views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('summary/', include(bets_urls)),
    path('market/', include(market_urls)),
    path('accounts/', include(accounts_urls)),
    path('betting_tools/', include(tools_urls)),
    ###### BLOG ######
    path('blog/sitemap.xml', wagtail_sitemap),
    path('blog/comments/', include('fluent_comments.urls')),
    path('blog_admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('blog/', include(wagtailimportexport_urls)),
    path('blog/', include(wagtail_urls)),
    ###### FLATPAGES #####
    path('privacy-policy/', views.flatpage, {'url': '/privacy-policy/'}, name='privacy'),
    path('cookie-policy/', views.flatpage, {'url': '/cookie-policy/'}, name='cookie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
