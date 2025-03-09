from django.urls import path
from . import views


urlpatterns = [
    path('items', MenuItemsView.as_view()),
    path('items/<int:pk>', MenuItemDetailView.as_view()),
]