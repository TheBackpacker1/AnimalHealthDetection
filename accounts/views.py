from django.db import models
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions  import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from MongoConnection import User_Collection
# Create your models here.



@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        is_admin = data.get('is_admin', False)

        try:
            # Hash the password before storing
            hashed_password = make_password(password)

            user = User.objects.create_user(
                email=email,
                password=hashed_password,
                is_staff=is_admin
            )

            # Send a welcome email (consider using a template for better formatting)
            html_message = render_to_string('welcome_email.html', {'user': user})
            send_mail(
                'Welcome to Our App',
                'Welcome to our app! Your account has been created.',
                'your_email@example.com',
                [email],
                html_message=html_message,
                fail_silently=False
            )

            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def get_user(request):
    if request.method == 'GET':
        email = request.GET.get('email')

        try:
            user = User.objects.get(email=email)
            user_data = {
                'email': user.email,
                'is_admin': user.is_staff
            }
            return JsonResponse(user_data)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 
 str(e)}, status=500)




@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                # Successful login, implement authentication logic (e.g., session-based or token-based)
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)



@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        new_email = data.get('new_email')
        new_password = data.get('new_password')

        try:
            user = User.objects.get(email=email)

            if new_password:
                # Hash the new password before updating
                new_hashed_password = make_password(new_password)
                user.password = new_hashed_password

            if new_email:
                user.email = new_email

            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, 
 status=400)
 
@csrf_exempt
def delete_user(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        email = data['email']

        try:
            user = User.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 
 str(e)}, status=500)