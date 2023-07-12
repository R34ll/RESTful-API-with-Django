from django.urls import path
from . import views


urlpatterns =[
    path("users/",view=views.show_users,name="show_user"),
    path("users/add/",view=views.add_user,name="add_user"),

    path("users/update/<int:user_id>/",view=views.put_user,name="put_users"), 
    path("users/del/<int:user_id>/",view=views.delete_user, name="delete_user"),
    path("",view=views.redirect_users),

]