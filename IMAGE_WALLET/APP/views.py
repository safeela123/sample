from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def reg(request):
    if request.method=='POST':
        uname=request.POST['uname']
        email=request.POST['email']
        psw=request.POST['password']
        cnf_psw=request.POST['cnf_password']
        if psw==cnf_psw:
            data=wallet.objects.create(uname=uname,email=email,psw=psw)
            data.save()
            return redirect(login)
        else:
            print("password or email doesnt match")
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        psw=request.POST['password']
        try:
            data=wallet.objects.get(email=email,psw=psw)
            request.session['user']=email
            return redirect(main)
        except:
            return redirect(login)
        
    return render(request,'login.html')

def main(request):
   
    if 'user' in request.session:
            user=wallet.objects.get(email=request.session['user']) # here getting loggined user using session email
            data=File.objects.filter(user=user) #here filtering user from database.so all users have unique main page.no one can see others uploaded pics
            return render(request,'main.html',{'data':data})
    else:
        return redirect(login)
        

def add(request):
    if 'user' in request.session:
        
        user1=wallet.objects.get(email=request.session['user'])
        if request.method =='POST':
            doc=request.FILES['doc']
            des=request.POST['des']
            data=File.objects.create(document=doc,describe=des,user=user1)
            data.save()
            return redirect(main)

        return render(request,'imageadd.html')
    else:
        return redirect(login)


def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect(login)
    else:
        return redirect(login)

def delete(request,pk):
    
        File.objects.filter(pk=pk).delete()
        return redirect(main)
        

def delete1(request):
    if 'user' in request.session:
            user=wallet.objects.get(email=request.session['user'])
            data=File.objects.filter(user=user)
            return render(request,'delete.html',{'data':data})
    else:
        
        return redirect(login)
      

