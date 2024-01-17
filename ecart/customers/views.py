from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.contrib import messages

# Create your views here.


def sign_out(request):
    logout(request)
    return redirect("home")


def show_account(request):
    context = {}
    if (
        request.POST and "register" in request.POST
    ):  # request.POST is a dictionary, and register is a key in the dictionary
        context["register"] = True
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            # print(username, password, email, address, phone)

            # create users accounts
            user = User.objects.create_user(
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
            success_message = "Account created successfully"
            messages.success(request, success_message)
        except Exception as e:
            print(e)
            error_message = "Duplicate username or invalid email"
            messages.error(request, error_message)

    if request.POST and "login" in request.POST:
        context["register"] = False
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid username or password"
            messages.error(request, error_message)

    return render(request, "account.html", context)
