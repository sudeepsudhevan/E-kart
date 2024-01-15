from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages

# Create your views here.


def show_account(request):
    if (
        request.POST and "register" in request.POST
    ):  # request.POST is a dictionary, and register is a key in the dictionary
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            # print(username, password, email, address, phone)

            # create users accounts
            user = User.objects.create(
                username=username,
                password=password,
                email=email,
            )

            # create customer account
            customer = Customer.objects.create(
                # name=username,
                address=address,
                phone=phone,
                user=user,
            )
            return redirect("home")
        except Exception as e:
            print(e)
            error_message = "Duplicate username or invalid email"
            messages.error(request, error_message)

    return render(request, "account.html")
