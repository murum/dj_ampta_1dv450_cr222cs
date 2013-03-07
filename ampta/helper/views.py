from ampta.models import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

def login_user(request):
	message = ''
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username_to_try = form.cleaned_data["username"]
			password_to_try = form.cleaned_data["password"]

			user = authenticate(username=username_to_try, password=password_to_try)
			if user is not None:
				if user.is_active:
					login(request, user)					
					return redirect('login')
				else:
					message = "Your account is not enabled"
			else:
				message = "Wrong username or password"
	else:
		form = LoginForm()
		
	context = {'form': form, 'message': message}
	return render(request, 'helper/login.html', context)

def logout_user(request):
	logout(request)
	return redirect('login')