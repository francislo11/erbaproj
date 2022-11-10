from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name="contacts"),
    path('inquiry/', views.inquiry, name="inquiry"),
    path('<str:pk>/', views.TaskDetail, name="dashboard"),
    path('update/<int:id>', views.update, name="update"),
    path('update/updaterecord/<int:id>',
         views.updaterecord, name="updaterecord"),
    path('delete/<int:id>', views.delete, name="delete"),

]
