from django.shortcuts import render, redirect
from .models import User, Customer

# Create your views here.

def create_customer(request):
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

