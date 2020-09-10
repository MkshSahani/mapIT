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
            gender_ = request.POST.get("singupGender")  # fetch the user City.
            age_ = request.POST.get("signupAge")
            print(username_)
            print(password_)
            print(email_)
            print(gender_)
            print(age_)
            username_ = username_.split(" ") # get the user name string in list. 
            firstname_ = username_[0] # get the element in the first element firstname
            lastname_ = "".join(username_[1:]) # rest of string is lastname
            newUser = User.objects.create_user(email_, email_, password)  # new user in user DataBase
            newUser.first_name = firstname_ 
            newUser.last_name = lastname_
            newUser.save() # user is saved here.
            # need to store the user in seprate table contain userAge, usrCity
            newUserData = models.UserData(userName=email_, userAge=age_, userGender=gender_)
            # save new user.
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
