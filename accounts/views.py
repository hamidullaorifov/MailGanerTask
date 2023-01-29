from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate





# Create your views here.



def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        data = request.POST
        form = CreateUserForm(data)
        password1 = data['password1']
        password2 = data['password2']
        if form.is_valid():
            if password1==password2:
                form.save()
                return redirect('login')
            
    return render(request,'accounts/register.html',{'form':form})


def loginview(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'accounts/login.html')
