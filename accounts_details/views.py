from django.shortcuts import render, redirect
from .models import User, Customer
from django.contrib.auth.models import user # small u
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.

def create_customer(request):
        if user.is_authenticated:
            if request.method == 'POST':
                data = request.data
                user_data = {
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'email': data['email'],
                    'mobile_no': data['mobile_no']
                }
                print(user_data)
                try:
                    # Check if user with the given email or mobile_no already exists
                    user = User.objects.get(Q(email=data['email']) | Q(mobile_no=data['mobile_no']))
                except User.DoesNotExist:
                    # If user does not exist, create a new user
                    user = User.objects.create(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'], mobile_no=user_data['mobile_no'])
                    try:
                        profile_no = Customer.objects.latest('profile_number') 
                    except:
                        profile_no = 5000
                    Customer.objects.create(user= user, profile_number=profile_no + 1)
                else:
                    pass
                    #retun warning email or mobile number is same
            else:
                pass
                #return UI for fill the details to create a customer
        else:
            return redirect('signup')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('create-customer/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST': #becose at submit time alway used post call
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                print('Username already exist')
                messages.info(request,"Uername already Taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print('Email already exist')
                messages.info(request,"Email already Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name , last_name=last_name, username=username, email=email, password=password_1)
                user.save();
                print('new user is created')
                return redirect('login')
            pass
        else:
            print('Password is not matching')
            messages.info(request, 'Password is not matching')
            return redirect('signup')
    else:  #at login time for UI alway use get call
        pass
        #return render(request, 'signup.html')