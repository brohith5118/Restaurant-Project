from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('add',views.add_item),
    path('manager_view',views.manager_view,name='manager_view'),
    path('delete/<int:id>',views.delete_item),
    path('open_edit/edit/<int:id>',views.edit_item),
    path('open_edit/<int:id>',views.open_edit),
]