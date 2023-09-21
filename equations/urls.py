from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from equations import views

urlpatterns = [
    path('add-vehicle/', views.add_vehicle),
    path('view-vehicles/', views.view_vehicles),
    path('delete-vehicle/<int:vehicle_id>/', views.delete_vehicle),
    path('edit-vehicle/<int:vehicle_id>/', views.edit_vehicle),
]

urlpatterns = format_suffix_patterns(urlpatterns)
