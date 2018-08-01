from django.urls import path

from market import views

urlpatterns = [
    path('create_new', views.new_market, name='new_market'),
    path('market_manual/<item_id>/<bet_type>/', views.market_manual, name='market_manual'),
    path('market_manual/', views.market_manual, name='market_manual'),
]
