from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from product.models import Product 
from warehouseStore.models import Warehouseinv
from django.utils import timezone

# Create your views here.

def product_detail(request, p_id):
    product = Product.objects.values('p_id','p_name', 'instore_price', 'manufacturer__manufacturer_name').get(p_id = p_id)
    return render(request, 'product_detail.html', {'product_detail' : product})

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
            return redirect('/user')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

# home
def home(request):
    product_list = Product.objects.order_by('p_id')
    if request.user.is_authenticated:
        try:
            cur_user = Member.objects.get(m_id = request.user.username)
            context = {'username': cur_user.get_name(), 'product_list':product_list} 
            return render(request, 'home.html', context)
        except:
            return render(request, 'home.html', {'product_list':product_list})
    else:
        return render(request, 'home.html', {'product_list':product_list} )


def cart(request):
    if request.user.is_authenticated: 
        cart_list = Cart.objects.filter(m = request.user.username)
            
        context = {
            'cart_list' : cart_list
        }
    return render(request, 'cart.html', context)


def card(request):
    if request.user.is_authenticated:
        cur_user = request.user.username
        mem = Member.objects.get(m_id = cur_user)
        card_list = Membercardinfo.objects.filter(m_id = mem)
        print(card_list)
        context = {'card_list' : card_list}
        return render(request, 'card.html', context)
        
    
def address(request):
    if request.user.is_authenticated:
        cur_user = request.user.username
        mem = Member.objects.get(m_id = cur_user)
        address_list = Memberaddress.objects.filter(m_id = mem)
        context = {'address_list' : address_list}
        return render(request, 'address.html', context ) 
    

def edit(request):    
    cur_user = request.user.username
    member = Member.objects.get(m_id = cur_user)
    if request.method == 'POST':
        new_email = request.POST['email']
        new_phone = request.POST['phone']
        type = request.POST['type']
        member.email = new_email
        member.phone = new_phone
        member.type = type
        member.save()
        return redirect('/')  
    else:
        context = {'member': member}
        return render(request, "edit.html", context)

def add_card(request):
    cur_user = request.user.username
    card_list = Membercardinfo.objects.filter(m = cur_user)
    print(type(cur_user))
    if request.method == 'POST':
        try:
            new_card = request.POST['cardnumber']
            if new_card == "":
                return card(request)
            new_cardholder = request.POST['cardholder']
            new_exp_month = request.POST['month']
            new_exp_year = request.POST['year']
            n_card = Membercardinfo(
                id = len(card_list)+1,
                m_id = cur_user,
                card_num = new_card,
                card_name = new_cardholder,
                card_exp_month= new_exp_month,
                card_exp_year= new_exp_year
            )
            n_card.save()
            return card(request)
        except Exception as e:
            print(e)
            return card(request)
    else:
        return render(request, "new_card.html") 
    

def add_address(request):
    cur_user = request.user.username
    mem = Member.objects.get(m_id = cur_user)
    add_list = Memberaddress.objects.filter(m_id = mem)
    if request.method == 'POST':
        try:
            address1 = request.POST['street']
            if address1 == "":
                return address(request)
            address2 = request.POST['box']
            state = request.POST['state']
            zip_code = request.POST['zip']
            n_add = Memberaddress(
                id = len(add_list)+1,
                m_id = cur_user,
                address1 = address1,
                address2 = address2,
                state= state,
                zipcode = zip_code
            )
            n_add.save()
            add_list = Memberaddress.objects.filter(m_id = mem)
            context = {'address_list' : add_list}
            return render(request, 'address.html', context)
        except Exception as e:
            print(e)
            return address(request)
    else:
        return render(request, "new_address.html") 

