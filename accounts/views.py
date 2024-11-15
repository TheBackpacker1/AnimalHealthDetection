from django.db import models
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from MongoConnection import User_Collection
# Create your models here.



@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email=data['email']
        password=data['password']
        is_admin=data.get('is_admin',False)
         

    user = User.create_user(email=email, password=password, is_admin=is_admin)




    send_mail(
         'AHD Your Account Credentials',
         f'Your account has been created. \nEmail:{email} \nPassword: {password} ',
         settings.EMAIL_HOST_USER,
         [email],
         fail_silently=False,

    )

    return JsonResponse({"message":"User created successfully and email sent . "})






@csrf_exempt
def get_user(request):
    if request.method == 'GET':
        email= request.GET.get('email')
        user= User_Collection.find_one({"email":email})


        if user:

            user_data = { 

                "email":user["email"],
                "is_admin":user["is_admin"],
            }
            return JsonResponse(user_data)
        
        else:
            return JsonResponse({"message":"User not found"},status=400)
        






@csrf_exempt


def login_user(request):

    if request.method == 'POST':
        data=json.loads(request.body)
        email=data['email']
        password=data['password']



        if User.verify_password(email,password):
            return JsonResponse({"message":"Login successful"})
        
        return JsonResponse({"message":"Invalid credentials"},status=400)
    





@csrf_exempt


def update_user(request):

    if request.method == 'POST':
        data=json.loads(request.body)
        email =data['email']
        new_email =data.get ('new_email')
        new_password= data.get('new_password')




        User.update_user(email,new_email,new_password)



        return  JsonResponse({"message":"User updated successfully"})
    


@csrf_exempt
def delete_user(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        email = data['email']
        
        result = User_Collection.delete_one({"email": email})
        
        if result.deleted_count > 0:
            return JsonResponse({"message": "User deleted successfully"})
        else:
            return JsonResponse({"message": "User not found"}, status=404)
