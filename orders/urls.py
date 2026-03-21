from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('add',views.add_item),
    path('manager_view',views.manager_view),
    path('delete/<int:id>',views.delete_item)
]