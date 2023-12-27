from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name ="index"),
    path('crud/', views.IndexResponses.as_view(),name ="index"),
    path('crud/delete/<int:id>', views.IndexDeleteResponse.as_view(),name ="index")
]