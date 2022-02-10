from django.urls import path
from customers import views

app_name='customers'

urlpatterns = [
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_logout/', views.employee_logout, name='employee_logout'),
    path('customer_order/', views.customer_order_view, name='customer_order_view'),
    path('customer_order/all_orders/', views.all_orders, name='all_orders'),
    path('customer_order/all_orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
]
