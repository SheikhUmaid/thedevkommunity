from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
# Create your views here.


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username)
            print(password)
            messages.success(request,f'Account has been created successfully! Login now')
            return redirect('devbase:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)             
    else:
        form = UserRegisterForm()
    
    return render(request,'devusers/register.html',{'form':form})


@login_required
def profile(request):
    return render(request, "devusers/profile.html")




@login_required
def profile_update(request):
    if request.method == 'POST':

        U_form = UserUpdateForm(request.POST, instance=request.user)
        P_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if U_form.is_valid() and P_form.is_valid():
            U_form.save()
            P_form.save()
            messages.success(request, "Updated successfully")
            return redirect('profile')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        U_form = UserUpdateForm(request.POST, instance=request.user)
        P_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

    context = {
        'u_form':U_form,
        'p_form':P_form
    }
    return render(request, "devusers/update.html",context)