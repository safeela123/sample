from django.urls import path
from . import views

urlpatterns=[
    path('register',views.reg),
    path('',views.login),
    path('main',views.main),
    path('add',views.add),
    path('logout',views.logout),
    path('delete/<pk>',views.delete),
    path('delete',views.delete1)
]