from django.urls import path

from . import views

urlpatterns = [
    # path('<int:class>',views.index),
    path("", views.index),
    path("<int:stuclass>/<str:sub>", views.contents, name='sub_contents'),
    path("<int:stuclass>/<str:sub>/addchapter",
         views.add_chapter, name='add_chapter'),
    path("<int:stuclass>/<str:sub>/<int:chapter>",
         views.chapter, name="sub_chapter"),
    path("material/<path:material_link>", views.material),
]
