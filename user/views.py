from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Member, Cart
from product.models import Product 
from django.utils import timezone
# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'])
            
            auth.login(request, user)
    
            member = Member(
                m_id = request.POST['username'],
                password = request.POST['password1'],
                name = request.POST['name'],
                phone = request.POST['phone'],
                email = request.POST['email'],
                type = request.POST['type'],
                user_status = 1,
                reg_date = timezone.now(),
                billing_date  = timezone.now(),
            )
            member.save()
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

# home
def home(request):
    if request.user.is_authenticated:
        cur_user = Member.objects.get(m_id = request.user.username)
        context = {'username': cur_user.get_name()} 
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def cart(request):
    if request.user.is_authenticated: 
        cur_user = request.user.username
        cart_list = Cart.objects.filter(m_id = request.user.username)
            
        context = {
            'cart_list' : cart_list
        }
    return render(request, 'cart.html', context)