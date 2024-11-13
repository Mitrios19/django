from django.urls import path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView
from . import views

app_name = 'shop'

urlpatterns = [
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('', HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('search', SearchView.as_view(), name='search'),
]
