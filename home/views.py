from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.template import loader

from .models import User,ROLES


def show_users(request):
    if request.method != "GET":
        return redirect("/users")
    

    template = loader.get_template("index.html")
    context = {"users":User.objects.all()}
    return HttpResponse(template.render(context,request))

@csrf_exempt
def add_user(request):
    if request.method != "POST":
        return redirect("/users")
    
    
    params = QueryDict(request.body.decode("utf-8"))

    username_param = params.get("username")
    email_param = params.get("email")
    role_param = params.get("role")

    if username_param == None or email_param == None or role_param not in ROLES:
        return redirect("/users")
    


    new_user = User(
        username=username_param[0].capitalize() + username_param[1:], 
        email=email_param,
        role=role_param,
        created_at=datetime.now()
    )
    new_user.save()

    return redirect("/users")


@csrf_exempt 
def put_user(request,user_id):
    if request.method != "POST" or request.POST["_method"] != "PUT":
        return redirect("/users")
    

    params =  None
    try:
        params = QueryDict(request.body.decode("utf-8"))
    except User.DoesNotExist:
        return redirect("/users")
    

    username_param = params.get("username")
    email_param = params.get("email")
    role_param = params.get("role")

    user = User.objects.get(id=user_id)

    if username_param != None and len(username_param) >= 4:
        user.username = username_param
    if email_param != None and len(email_param) >= 4:
        user.email = email_param
    if role_param != None and role_param in ROLES:
        user.role = role_param
    
    user.save()
    return redirect("/users")


@csrf_exempt
def delete_user(request,user_id):
    if request.method != "POST" or request.POST["_method"] != "DEL":
        return redirect("/users")
    
    
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect("/users")
    
    except User.DoesNotExist:
        return redirect("/users")



def redirect_users(request):
    return redirect("/users")


