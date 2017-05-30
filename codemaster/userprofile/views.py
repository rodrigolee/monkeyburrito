from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate
from userprofile.forms import SignUpForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'userprofile/signup.html', {'form': form})
