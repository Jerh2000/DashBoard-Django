from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('births/', views.births, name='dashboard-births'),
    path('educationlevel/', views.educationlevel, name='dashboard-educationlevel'),
    path('flights/', views.flights, name='dashboard-flights'),

    
    path('births/delete/<int:pk>/', views.birth_delete,
         name='dashboard-births-delete'),
     path('educationslevel/delete/<int:pk>/', views.educationlevel_delete,
         name='dashboard-educationlevel-delete'),
     path('flights/delete/<int:pk>/', views.flights_delete,
         name='dashboard-flights-delete'),
    
    
    path('births/edit/<int:pk>/', views.birth_edit,
         name='dashboard-birth-edit'),    
     path('educationlevel/edit/<int:pk>/', views.educationlevel_edit,
         name='dashboard-educationlevel-edit'),
     path('flights/edit/<int:pk>/', views.flights_edit,
         name='dashboard-flights-edit'),

    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
]
