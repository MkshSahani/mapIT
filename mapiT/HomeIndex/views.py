from django.shortcuts import render
from django.contrib.auth.models import User 
from . import models
# Create your views here.

def indexHomePageRender(request): 
    context = {}
    ageList = [i for i in range(17, 90)]  # ageList
    context['ageList'] = ageList
    if request.method == "POST":
        username = request.POST.get("_username") # fetch the username.
        password = request.POST.get("_password")  # fetch the password.

        if username is None:
            print("<< === Signup requested... === >>")
            username_ = request.POST.get("signupUserName")  # fetch the signup username
            password_ = request.POST.get("signupUserPassword")  # fetch the password.
            email_ = request.POST.get("signupEmail")  # fetch the user email.
            city_ = request.POST.get("signupCity")  # fetch the user City.
            age_ = request.POST.get("signupAge")
            print(username_)
            print(password_)
            print(email_)
            print(city_)
            print(age_)
            username_ = username_.split(" ")
            firstname_ = username_[0]
            lastname_ = "".join(username_[1:])
            newUser = User.objects.create_user(email_, email_, password)  # new user
            newUser.first_name = firstname_
            newUser.last_name = lastname_
            newUser.save()
            newUserData = models.UserData(userName=email_, userAge=age_, userCity=city_)
            newUserData.save() # new User Data. 
            return render(request, 'HomePage.html', context)
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
