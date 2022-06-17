
from django.contrib import admin
from django.urls import path
from student_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("delete/<int:id>/", views.delete_data, name="delete_data"),
    path("update/<int:id>/", views.update_data, name="update_data"),
]
