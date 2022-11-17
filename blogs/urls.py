from django.urls import path
from .import views

# set the / api, as variable=index to callback function

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blogs/qt_01/ ', views.qt_01, name="qt_01"),
    path('blogs/qt_02/ ', views.qt_02, name="qt_02"),
    path('blogs/qt_01/QT/ ', views.QT, name="QT"),
    path('blogs/dt01/ ', views.qt_01, name="dt01"),
    path('blogs/rm01/ ', views.qt_02, name="rm01"),
]
