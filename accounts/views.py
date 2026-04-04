from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile
from .forms import SignForm
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():   # To validate
            # myform = form.save(commit=False)
            # myform.owner = request.user
            # myform.save()
            form.save()     # To save in database
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)   # To Check
            login(request,user)   #login
            return redirect(reverse('/accounts/profile'))     # To refresh
    else:
        form = SignForm()
    
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)