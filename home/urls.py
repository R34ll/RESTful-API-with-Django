from django.urls import path
from . import views


urlpatterns =[
    path("users/",view=views.show_users,name="show_user"), # GET /
    path("users/add/",view=views.add_user,name="add_user"), # POST /

    path("users/update/<int:user_id>/",view=views.put_user,name="put_users"), # PUT /update/id
    path("users/del/<int:user_id>/",view=views.delete_user, name="delete_user") # DEL /del/id

    # path("user/<int:user_id>/",view=views.put_user,name="put_user")

]