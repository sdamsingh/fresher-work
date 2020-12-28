from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import  studentRegistration
from .models import User
# Create your views here.

def Home(request):
    return render(request, 'accounts/base.html')
#this function will add new item and show n all the item
def add_show(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email = em, password = pw)
            reg.save()
            fm = studentRegistration()
    else:
        fm = studentRegistration()
       
    return render(request ,'accounts/addandshow.html',{'form':fm,'stu':stud})
    

#this function will delete data

def delete_data(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')


#this function will be used to update
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm=studentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=studentRegistration(instance=pi)
    return render(request,'accounts/updatefile.html',{'form':fm})


