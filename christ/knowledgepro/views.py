from django.shortcuts import render
from knowledgepro.forms import UserDetailsForm,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
    return render(request,'knowledgepro/home.html')
def register(request):

    registered =  False
    if request.method =='POST':

        user_form = UserForm(request.POST)
        details_form = UserDetailsForm(request.POST)

        if user_form.is_valid() and details_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            details = details_form.save(commit=False)
            details.user = user
            if 'display_pic' in request.FILES:
                details.display_pic = request.FILES['display_pic']
            details.save()

            registered = True
        else:
            print(user_form.errors,details_form.errors)
    else:
        user_form = UserForm()
        details_form = UserDetailsForm()

    return render(request,'knowledgepro/register.html',{'user_form':user_form,'registered':registered,'details_form':details_form})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("in active account")
        else:
            return HttpResponse('<h1>Invalid Login Credentials</h1>')
    else:
        return render(request,'knowledgepro/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
