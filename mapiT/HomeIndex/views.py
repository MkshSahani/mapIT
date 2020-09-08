from django.shortcuts import render

# Create your views here.

def indexHomePageRender(request): 
    context = {}
    if request.method == "POST":
        username = request.POST.get("_username") # fetch the username.
        password = request.POST.get("_password")  # fetch the password.

        if username is None:
            print("<< === Signup requested... === >>")
            return render(request, 'Hompage.html', context)
        else:

            _user = {
                'username': username,
                'password': password
            }
            print(_user)
            context['username'] = username
            context['password'] = password 
            return render(request, 'HomePage.html', context) # need to change a lot..
    else:
        return render(request, 'HomePage.html', context) # render the Homage page without user login.
