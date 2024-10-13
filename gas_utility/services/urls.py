from django.urls import path
from . import views

urlpatterns = [
    #user
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('profile/<int:customer_id>/', views.profile, name='profile'),
    #services
    path('create_service_request/', views.create_service_request, name='create_service_request'),
    path('all_requests/', views.service_request_success, name='service_request_success'),
    path('service-request/complete/<int:request_id>/', views.complete_service_request, name='complete_service_request'),
    path('service-request/track/<int:request_id>/', views.track_service_request, name='track_service_request'),
    path('admin_request_center/', views.admin_request_allrequest, name='admin_request_allrequest'),
    #Hoem route
    path('', views.home, name='home'),
]
