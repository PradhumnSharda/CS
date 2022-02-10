from django.urls import path
from tyre_stock import views

app_name = 'tyre_stock'

urlpatterns=[
    path('tyres/<int:pk>/', views.TyreDetailView.as_view(), name='tyre_detail'),
    path('', views.tyre_stock, name='tyre_stock'),
    path('create_or_update/', views.TyreCreateView.as_view(), name='tyre_create'),
    path('<int:pk>/update/', views.TyreUpdateView.as_view(), name='tyre_update'),
    path('<int:pk>/delete/', views.TyreDeleteView.as_view(), name='tyre_delete'),

    path('new_stock_view/', views.new_stock_view, name='new_stock_view'),
    path('all_new_stock/', views.all_new_stock, name='all_new_stock'),
    path('all_new_stock/<int:pk>', views.New_Stock_DetailView.as_view(), name='new_stock_detail'),
    path('<int:pk>/new_tyre_update/', views.NewTyreUpdateView.as_view(), name='new_stock_update'),

]
