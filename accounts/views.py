from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile
from .forms import SignForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():   # To validate
            form.save()     # To save in database
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)   # To Check
            login(request,user)   #login
            context = {'form':form}
            return redirect(reverse('/accounts/profile'), context)     # To refresh
    else:
        form = SignForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request, 'accounts/profile.html', context)



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)   # To appear saved data
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
            
    else:     # To show profile
        userform = UserForm(instance=request.user)   # To appear saved data
        profileform = ProfileForm(instance=profile)
        context = {'userform':userform, 'profileform':profileform}
    return render(request, 'accounts/profile_edit.html',context)