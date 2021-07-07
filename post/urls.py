from django.urls import path
from post import views


urlpatterns = [
    path('', views.HomeViews.as_view(), name='home'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail')
]