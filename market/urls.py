from django.urls import path

from market import views

urlpatterns = [
    path('create_new', views.new_market, name='new_market'),
    path('market_manual/', views.market_manual, name='market_manual'),
]
