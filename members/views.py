from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.success(request, ("There was an error during login"))
#             return redirect("login")
#     else:
#         return render(request, "authentication/login.html", {})
