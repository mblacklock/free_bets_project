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

from django.urls import path

from bets import views

urlpatterns = [
    path('create_new', views.new_summary, name='new_summary'),
    path('update/<param>', views.update_ajax, name='update_ajax'),
    path('action/<item_id>', views.action, name='action'),
    path('users/<email>/', views.my_summaries, name='my_summaries'),
    path('external/<slug>', views.affiliate_click, name='affiliate_click'),
    path('tracking/', views.tracking, name='tracking'),
    path('<summary_id>/', views.view_summary, name='view_summary'),
]
