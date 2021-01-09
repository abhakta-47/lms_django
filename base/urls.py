from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns=[
    # path('<int:class>',views.index),
    path("", views.index),
    path("<int:stuclass>/<str:sub>", views.contents),
    path("material/<path:material_link>", views.material)
]