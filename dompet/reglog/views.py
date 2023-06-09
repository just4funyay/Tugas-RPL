# Create your views here.
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from home import views as homeviews
# Create your views here.


def SignupPage(request):
    if request.method=='POST':
        uname1=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('passwordconfirm')
        if password=='' and password1=='' and uname1=='' and email=='':
            messages.info(request, 'isi dengan lengkap')
            string="*anda belum memasukkan apapun!"
            return render(request,'reg.html',{'string':string})
        elif password!=password1:
            string="*password tidak sama"
            return render(request,'reg.html',{'string':string})
        elif password==password1:
            if User.objects.filter(username=uname1).exists():
                return redirect(SignupPage)
            else:
                myuser=User.objects.create_user(uname1,email,password)
                myuser.save()
                return redirect(LoginPage)
            

    return render(request,'reg.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(homeviews.Homepage)
        else:
            string="*Username atau Password salah"
            return render(request,'log.html',{'string':string})
    return render(request,'log.html')
def logout(request):
    auth.logout(request)
    return redirect(LoginPage)
