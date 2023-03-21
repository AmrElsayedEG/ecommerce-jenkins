from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_process(request):
    if request.user.is_authenticated:
        return redirect(reverse('reports:dashboard'))
    message = None
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(request,username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('reports:dashboard'))
        message = "Wrong E-mail or Password"

    context = {'message' : message}
    return render(request, 'login.html', context)

@login_required
def logout_process(request):
    logout(request)
    return redirect(reverse('reports:login'))

def unauthorized(request):
    return render(request, '401.html')