from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to fetch the user by email (username parameter contains email)
            user = UserModel.objects.get(Q(email=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return render(request, 'scheduler/register.html', {'error': 'Passwords do not match'})
        
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            return render(request, 'scheduler/register.html', {'error': 'Email already exists'})
        
        try:
            user = UserModel.objects.create_user(username=email, email=email, password=password, first_name=first_name)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        except Exception as e:
            return render(request, 'scheduler/register.html', {'error': str(e)})
    
    return render(request, 'scheduler/register.html', {'title': 'Register'})