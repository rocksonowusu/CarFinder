from django.urls import path
from .views import home, recommend, results, car_detail, upcoming_features

urlpatterns = [
    path('', home, name='home'),
    path('recommend/', results, name='recommend'),
    path('results/', results, name='results'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),  # Add this
    path('features/', upcoming_features, name='upcoming_features'), 
]
