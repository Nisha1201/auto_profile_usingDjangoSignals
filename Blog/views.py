from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form,"hhhhhhhhhhhhhhhhhhhhhh")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
 
 
@login_required
def profile(request):
    if request.method == 'POST':
        # print("ygiiiiiiiiiiii")
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.save()

            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            # print(u_form,"user form")
            # print(p_form,"prifile form")
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
 
    return render(request, 'profile.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
                login(request, user)
                return redirect('profile')

        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login.html')
