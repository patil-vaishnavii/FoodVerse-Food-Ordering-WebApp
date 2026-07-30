from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def register(request):

  if request.method == "POST":

    form = RegistrationForm(request.POST)

    if form.is_valid():

      user = form.save()
      login(request,user)
      return redirect("/")

  else:
    form = RegistrationForm()

  return render(
    request, "accounts/register.html",
    {
      "form":form
    }
  )

def login_view(request):

  if request.method == "POST":

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():

      username = form.cleaned_data.get("username") # cleaned_data contains the validated values from the form.
      password = form.cleaned_data.get("password")

      user = authenticate(
        request,
        username=username,
        password=password
      )

      if user is not None:
        login(request,user) #Remember this user for future requests.

        return redirect("/")
      
  else: 
    form = AuthenticationForm()

  return render(
    request,
    "accounts/login.html",
    {
      "form": form
    }
  )

def logout_view(request):
  logout(request)
  return redirect("/")