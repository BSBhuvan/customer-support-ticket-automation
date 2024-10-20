from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User

def user_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        # Create a new user and save it to the database
        user = User(name=name, email=email, role=role)
        user.save()

        return redirect('/success/')  # Redirect to a success page after submission

    return render(request, 'tickets/form.html')

def success(request):
    return render(request, 'tickets/success.html')
