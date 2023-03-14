from django.shortcuts import render
from . forms import studentregistration
from django.http import HttpResponseRedirect
from . models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    data=User.objects.all()
    return render(request,"en/addsho.html",{"form":fm,"rec":data})

def del_user(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm = studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm = studentregistration(instance=pi)
            
    return render(request,'en/up.html',{"form":fm})